from datetime import date, timedelta
from time import sleep
import mechanize
from BeautifulSoup import BeautifulSoup
import MySQLdb
from random import shuffle, randint
    
def daterange(start_date, end_date):
    for n in range((end_date - start_date).days):
        yield start_date + timedelta(n)

start_date = date(1995, 1, 1)
end_date = date.today()

weekdays = []
for single_date in daterange(start_date, end_date):
    if single_date.weekday() not in (5,6) :
        weekdays.append(single_date)
        
db = MySQLdb.connect(db="civil_jury",
                     read_default_file="~/.my.cnf")
c = db.cursor()
c.execute("select distinct date_filed from cases")
scraped_days = c.fetchall()
scraped_days = set([day[0] for day in scraped_days])

c.close()

weekdays = list(set(weekdays).difference(scraped_days))


holidays = set([
    date(1995, 1, 2),
    date(1995, 1, 16),
    date(1995, 2, 13),
    date(1995, 2, 20),
    date(1995, 3, 6),
    date(1995, 5, 29),
    date(1995, 7, 4),
    date(1995, 9, 4),
    date(1995, 10, 9),
    date(1995, 11, 3),
    date(1995, 11, 10),
    date(1995, 11, 23),
    date(1995, 11, 24),
    date(1995, 12, 25),
    date(1996, 1, 1),
    date(1996, 1, 15),
    date(1996, 2, 12),
    date(1996, 2, 19),
    date(1996, 3, 4),
    date(1996, 5, 27),
    date(1996, 7, 4),
    date(1996, 9, 2),
    date(1996, 10, 14),
    date(1996, 11, 5),
    date(1996, 11, 11),
    date(1996, 11, 28),
    date(1996, 11, 29),
    date(1996, 12, 25),
    date(1996, 12, 25),
    date(1997, 1, 1),
    date(1997, 1, 20),
    date(1997, 2, 12),
    date(1997, 2, 17),
    date(1997, 3, 3),
    date(1997, 5, 26),
    date(1997, 7, 4),
    date(1997, 9, 1),
    date(1997, 10, 13),
    date(1997, 11, 11),
    date(1997, 11, 27),
    date(1997, 11, 28),
    date(1997, 12, 25),
    date(1998, 1, 1),
    date(1998, 1, 19),
    date(1998, 2, 12),
    date(1998, 2, 16),
    date(1998, 3, 2),
    date(1998, 5, 25),
    date(1998, 7, 3),
    date(1998, 9, 7),
    date(1998, 10, 12),
    date(1998, 11, 3),
    date(1998, 11, 11),
    date(1998, 11, 26),
    date(1998, 11, 27),
    date(1998, 12, 25),
    date(1999, 1, 1),
    date(1999, 1, 18),
    date(1999, 2, 12),
    date(1999, 2, 15),
    date(1999, 3, 1),
    date(1999, 5, 31),
    date(1999, 7, 5),
    date(1999, 9, 6),
    date(1999, 10, 11),
    date(1999, 11, 11),
    date(1999, 11, 25),
    date(1999, 11, 26),
    date(1999, 12, 24),
    date(1999, 12, 31),
    date(2000, 1, 17),
    date(2000, 2, 11),
    date(2000, 2, 21),
    date(2000, 3, 6),
    date(2000, 5, 29),
    date(2000, 7, 4),
    date(2000, 9, 4),
    date(2000, 10, 9),
    date(2000, 11, 7),
    date(2000, 11, 10),
    date(2000, 11, 23),
    date(2000, 11, 24),
    date(2000, 12, 25),
    date(2001, 1, 1),
    date(2001, 1, 15),
    date(2001, 2, 12),
    date(2001, 2, 19),
    date(2001, 3, 5),
    date(2001, 5, 28),
    date(2001, 7, 4),
    date(2001, 9, 3),
    date(2001, 10, 8),
    date(2001, 11, 12),
    date(2001, 11, 22),
    date(2001, 11, 23),
    date(2001, 12, 25),
    date(2002, 1, 1),
    date(2002, 1, 21),
    date(2002, 2, 12),
    date(2002, 2, 18),
    date(2002, 3, 4),
    date(2002, 5, 27),
    date(2002, 7, 4),
    date(2002, 9, 2),
    date(2002, 10, 14),
    date(2002, 11, 5),
    date(2002, 11, 11),
    date(2002, 11, 28),
    date(2002, 11, 29),
    date(2002, 12, 25),
    date(2003, 1, 1),
    date(2003, 1, 20),
    date(2003, 2, 12),
    date(2003, 2, 17),
    date(2003, 3, 3),
    date(2003, 5, 26),
    date(2003, 7, 4),
    date(2003, 9, 1),
    date(2003, 10, 13),
    date(2003, 11, 11),
    date(2003, 11, 27),
    date(2003, 11, 28),
    date(2003, 12, 25),
    date(2004, 1, 1),
    date(2004, 1, 19),
    date(2004, 2, 12),
    date(2004, 2, 16),
    date(2004, 3, 1),
    date(2004, 5, 31),
    date(2004, 7, 5),
    date(2004, 9, 6),
    date(2004, 10, 11),
    date(2004, 11, 2),
    date(2004, 11, 11),
    date(2004, 11, 25),
    date(2004, 11, 26),
    date(2004, 12, 24),
    date(2004, 12, 31),
    date(2005, 1, 17),
    date(2005, 2, 11),
    date(2005, 2, 21),
    date(2005, 3, 7),
    date(2005, 5, 30),
    date(2005, 7, 4),
    date(2005, 9, 5),
    date(2005, 10, 10),
    date(2005, 11, 11),
    date(2005, 11, 24),
    date(2005, 11, 25),
    date(2005, 12, 26),
    date(2006, 1, 2),
    date(2006, 1, 16),
    date(2006, 2, 13),
    date(2006, 2, 20),
    date(2006, 3, 6),
    date(2006, 5, 29),
    date(2006, 7, 4),
    date(2006, 9, 4),
    date(2006, 10, 9),
    date(2006, 11, 7),
    date(2006, 11, 10),
    date(2006, 11, 23),
    date(2006, 11, 24),
    date(2006, 12, 25),
    date(2007, 1, 1),
    date(2007, 1, 15),
    date(2007, 2, 12),
    date(2007, 2, 19),
    date(2007, 3, 5),
    date(2007, 5, 28),
    date(2007, 7, 4),
    date(2007, 9, 3),
    date(2007, 10, 8),
    date(2007, 11, 12),
    date(2007, 11, 22),
    date(2007, 11, 23),
    date(2007, 12, 25),
    date(2008, 1, 1),
    date(2008, 1, 21),
    date(2008, 2, 12),
    date(2008, 2, 18),
    date(2008, 3, 3),
    date(2008, 5, 26),
    date(2008, 7, 4),
    date(2008, 9, 1),
    date(2008, 10, 13),
    date(2008, 11, 4),
    date(2008, 11, 11),
    date(2008, 11, 27),
    date(2008, 11, 28),
    date(2008, 12, 25),
    date(2009, 1, 1),
    date(2009, 1, 19),
    date(2009, 2, 12),
    date(2009, 2, 16),
    date(2009, 3, 2),
    date(2009, 5, 25),
    date(2009, 7, 3),
    date(2009, 9, 7),
    date(2009, 10, 12),
    date(2009, 11, 11),
    date(2009, 11, 26),
    date(2009, 11, 27),
    date(2009, 12, 25),
    date(2010, 1, 1),
    date(2010, 1, 18),
    date(2010, 2, 12),
    date(2010, 2, 15),
    date(2010, 3, 1),
    date(2010, 5, 31),
    date(2010, 7, 5),
    date(2010, 9, 6),
    date(2010, 10, 11),
    date(2010, 11, 11),
    date(2010, 11, 25),
    date(2010, 11, 26),
    date(2010, 12, 24),
    date(2010, 12, 31),
    date(2011, 1, 17),
    date(2011, 2, 11),
    date(2011, 2, 21),
    date(2011, 3, 7),
    date(2011, 5, 30),
    date(2011, 7, 4),
    date(2011, 9, 5),
    date(2011, 10, 10),
    date(2011, 11, 11),
    date(2011, 11, 24),
    date(2011, 11, 25),
    date(2011, 12, 26)
])


missing_days = set([
date(2011, 2, 3),
date(2011, 2, 2),
date(1996, 4, 5),
date(1995, 4, 14),
date(1996, 3, 19),
date(1997, 3, 28)
])

case_summary_days = set([
date(2011,11,4),
date(2001,9,11)
])

weekdays = list(set(weekdays).difference(holidays))
weekdays = list(set(weekdays).difference(missing_days))
weekdays = list(set(weekdays).difference(case_summary_days))
shuffle(weekdays)
print len(weekdays)
for day in sorted(weekdays) :
    print day
    print day.weekday()

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

daily_cases_url = "https://w3.courtlink.lexisnexis.com/cookcounty/FindDock.asp?NCase=&SearchType=1&Database=2&case_no=&Year=&div=&caseno=&PLtype=1&sname=&CDate=%m/%d/%Y"

db = MySQLdb.connect(db="civil_jury",
                      read_default_file="~/.my.cnf")

c = db.cursor()


days_unscraped = weekdays
for filing_date in weekdays :
    try:
        page = br.open(filing_date.strftime(daily_cases_url))
        html = page.read()
        if 'not found. Please try again.' in html :
            print 'date missing'
            print filing_date
            sleep(randint(5,15))
            continue
        elif 'Case Information Summary for Case Number' in html:
            print 'case summary data'
            print filing_date
            sleep(randint(5,15))
            continue
        soup = BeautifulSoup(html)
        for row in soup.findAll("table")[1].findAll("tr") :
            case = [col.text for col in row.findAll("td")]
            [case_num, plaintiff, defendant] = case[0:3]
            try: 
                c.execute("""
                INSERT INTO cases (case_id, defendant, plaintiff,
                date_filed) VALUES (%s, %s, %s, %s)
                """, (case_num, defendant, plaintiff, filing_date)
                          )
            except MySQLdb.IntegrityError :
                continue
        sleep(randint(5,15))
#    except IOError as e:
    except Exception as e:
        print e
        print html
        break




