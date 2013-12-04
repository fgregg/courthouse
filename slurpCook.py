import mechanize
import MySQLdb


br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

case_summary_url = "https://w3.courtlink.lexisnexis.com/cookcounty/FindDock.asp?NCase={0}&SearchType=0&Database=2&case_no=&=&=&=&PLtype=1&sname=&CDate="

db = MySQLdb.connect(db="civil_jury",
                     read_default_file="~/.my.cnf")
c = db.cursor()
c.execute("select case_id from cases where case_id not in (select case_id from cases_html)")

case_ids = [row[0] for row in c.fetchall()]

for case_id in case_ids[0:1] :
    page = br.open(case_summary_url.format(case_id))
    html = page.read()    
    c.execute("""insert into cases_html (case_id, html) values (%s,%s)""",
              (case_id, html.strip())
              )

c.close()
