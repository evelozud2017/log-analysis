#!/usr/bin/env python3
import psycopg2

DBNAME = "news"


def get_top_articles(list_count):
    """Return article and number of times viewed with most viewed first."""
    query = """
        select a.title, sum(alv.views) as views from articles a,
         article_log_view alv where a.slug = alv.article
         group by a.title
         order by sum(alv.views) desc limit %s;"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query, (list_count,))
    rows = c.fetchall()
    db.close()
    return rows


def get_top_authors():
    """Return author and number of views with most viewed first."""
    query = """
        select au.name, sum(alv.views) as views
         from articles a inner join article_log_view alv
         on a.slug = alv.article
         inner join authors au
         on a.author = au.id
         group by au.name
         order by sum(alv.views) desc;"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


def get_most_error_day():
    """Return day with errors > 1%."""
    query = """
        select to_char(tot.logdate, 'FMMonth DD, YYYY') as logdate,
         round(((err.errors_count::decimal/tot.requests_count)*100),2)
         as err_pct
         from
         ( select date(time) as logdate,
         count(*) as requests_count
         from log
         group by date(time) ) tot,
        ( select date(time) as logdate,
         count(*) as errors_count
         from log
         where status <> '200 OK'
         group by date(time) ) err
         where
         tot.logdate = err.logdate
         and (err.errors_count::decimal/tot.requests_count) > .01;"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


def print_top_articles(list_count):
    """Prints the articles and number of times viewed."""
    print("What are the most popular %d articles of all time?\n" % list_count)
    top_articles = "\"%s\" - %d views\n"
    results = "".join(
        top_articles % (title, views) for title, views in get_top_articles(
            list_count))
    print(results)


def print_top_authors():
    """Prints the author and total times their article were viewed."""
    print("What are the most popular article authors of all time?\n")
    top_authors = "%s - %d views\n"
    results = "".join(
        top_authors % (name, views) for name, views in get_top_authors())
    print(results)


def print_top_errors():
    """Prints day(s) where requests had more than 1 percent error."""
    print("On which days did more than 1% of requests lead to errors?\n")
    top_authors = "%s - % 6.2f%% errors\n"
    results = "".join(
        top_authors % (
            logdate, err_pct) for logdate, err_pct in get_most_error_day())
    print(results)


if __name__ == "__main__":
    """Call print methods"""
    print_top_articles(3)
    print_top_authors()
    print_top_errors()
