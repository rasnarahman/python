from django.http import HttpResponse
from django.shortcuts import render
import pymysql


def query_mysql(query):
    cnx = pymysql.connect( user='root',password='Ottawa2018',host='localhost',database='assignment1')
    cursor = cnx.cursor ()
    cursor.execute ( query )
    header = [i[0] for i in cursor.description]
    rows = [list ( i ) for i in cursor.fetchall ()]
    rows.insert ( 0,header )
    cursor.close ()
    cnx.close ()
    return rows


def sqllist_to_html(list2d):
    htable = u'<table border="1" bordercolor=000000 cellspacing="0" cellpadding="1" ' \
             u'style="table-layout:fixed;vertical-align:bottom;font-size:13px;font-family:verdana,sans,' \
             u'sans-serif;border-collapse:collapse;border:1px solid rgb(130,130,130)" > '
    list2d[0] = [u'<b>' + i + u'</b>' for i in list2d[0]]

    for row in list2d:
        newrow = u'<tr>'
        newrow += u'<td align="left" style="padding:1px 4px">' + str ( row[0] ) + u'</td>'
        row.remove ( row[0] )
        newrow = newrow + ''.join (
            [u'<td align="right" style="padding:1px 4px">' + str ( x ) + u'</td>' for x in row] )
        newrow += '</tr>'
        htable += newrow
    htable += '</table>'
    return htable


def html_sql(query):
    return sqllist_to_html (query_mysql ( query ) )


query = "select * from tunas"


def index(request):  # method return HttpRepsonse with html content
    return HttpResponse ( "CST8333 exexcise4: PET DATA, Rasna Rahman\n\n" + html_sql(query))
