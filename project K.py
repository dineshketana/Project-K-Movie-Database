
import mysql.connector as mc
mycon=mc.connect(host='localhost',user='root',passwd='pass',database='movies')
cur=mycon.cursor()
#to add something
def add():
    m_id=input('enter movie ID-')
    mov=input('enter movie name-')
    if mov==None:
        mov="Null"
    dirt=input('enter director name-')
    if dirt==None:
        dirt="Null"
    prod=input('enter producer name-')
    if prod==None:
        prod="Null"
    prod_h=input('enter production house name-')
    if prod_h==None:
        prod_h="Null"
    mdir=input('enter music director name-')
    if mdir==None:
        mdir="Null"
    hero=input('enter hero name-')
    if hero==None:
        hero="Null"
    hrn=input('enter heroine name-')
    if hrn==None:
        hrn="Null"
    gen=input('enter movie genre-')
    if gen==None:
        gen="Null"
    clt=input('enter movie collections-')
    if clt==None:
        clt="Null"
    rel=input('enter date[dd-mm-yyyy]-')
    if rel==None:
        rel="Null"
    
    add="insert into movie values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(m_id,mov,dirt,prod,prod_h,mdir,hero,hrn,gen,clt,rel)
    cur.execute(add)
    print("ADDED SUCCESSFULLY")
    mycon.commit()


#to update something
def update():
    prk=input("enter primary key value")
    att=input("enter attribute name")
    val=input("enter updated value")
    upd="update movie set "+att+"='{}' where movie_id='{}'".format(val,prk)
    cur.execute(upd)
    print("UPDATED SUCCESSFULLY")
    mycon.commit()

#to search anything
def search(): 
    print("PRESS 1 TO SEARCH MOVIE NAME \nPRESS 2 TO SEARCH HERO NAME\nPRESS 3 TO SEARCH HEROINE NAME\nPRESS 4 TO SEARCH DIRECTOR NAME\nPRESS 5 TO SEARCH PRODUCER \nPRESS 6 TO SEARCH MUSIC DIRECTOR \nPRESS 7 TO SEARCH YEAR\nPRESS 8 TO SEARCH PRODUCTION HOUSE\nPRESS 9 TO SEARCH GENRE") 
    ch=int(input('ENTER YOUR CHOICE TO CONTINUE-'))
    if ch==1:
        sm=input('ENTER MOVIE NAME TO SEARCH-')
        movie='select * from movie where movie like "%{}%"'.format(sm)
        cur.execute(movie)
        data=cur.fetchall()
        for row in data:
            print('MOVIE NAME-',row[1],'\nHERO NAME-',row[6],'\nHEROINE NAME-',row[7],'\nDIRECTOR NAME-',row[2],'\nPRODUCER NAME-',row[3],'\nMUSIC DIRECTOR-',row[5],'\nRELEASED DATE-',row[10],'\nGENRE-',row[8],'\nPRODUCTION HOUSE-',row[4],'\nCOLLECTIONS-',row[9],end='\n\n') 
        mycon.commit()
    if ch==2:
        sh=input("ENTER HERO NAME TO SEARCH-")
        hero='select Movie from movie where Hero like "%{}%"'.format(sh)
        cur.execute(hero)
        data=cur.fetchall()
        print("MOVIES OF YOUR HERO:")
        for row in data:
            print(row[0]) 
        mycon.commit()
    if ch==3:
        she=input('ENTER HEROINE NAME TO SEARCH-')
        heroine='select movie from movie where Heroine like "%{}%"'.format(she)
        cur.execute(heroine)
        data=cur.fetchall()
        print("MOVIES OF YOUR HEROINE:")
        for row in data:
            print(row[0]) 
        mycon.commit()
    if ch==4:
        sd=input("ENTER DIRECTOR NAME TO SEARCH-")
        director='select movie from movie where Director like "%{}%"'.format(sd)
        cur.execute(director)
        data=cur.fetchall()
        print("MOVIES OF YOUR DIRECTOR:")
        for row in data:
            print(row[0]) 
        mycon.commit()
    if ch==7:
        sy=input("ENTER YEAR TO SEARCH-")
        year='select movie,Release_date from movie where Release_date like "%{}%"'.format(sy)
        cur.execute(year)
        data=cur.fetchall()
        print('THE MOVIES ARE AS FOLLOWS')
        for row in data:
            print(row[0],' ',row[1])  
        mycon.commit()
    if ch==9:
        sc=input("ENTER GENRE TO SEARCH-")
        cate='select movie,genre from movie where Genre like "%{}%"'.format(sc)
        cur.execute(cate)
        data=cur.fetchall()
        print('THE MOVIES ARE AS FOLLOWS')
        for row in data:
            print(row[0],' ',row[1]) 
        mycon.commit()
    if ch==8:
        si=input("ENTER PRODUCTION HOUSE TO SEARCH-")
        indy='select movie from movie where Production_house like "%{}%"'.format(si)
        cur.execute(indy)
        data=cur.fetchall()
        print('SEARCHED PRODUCTION HOUSE MOVIES ARE:')
        for row in data:
            print(row[0]) 
        mycon.commit()
    if ch==6:
        sr=input("ENTER MUSIC DIRECTOR TO SEARCH-")
        ratg='select movie from movie where Music_director like "%{}%"'.format(sr)
        cur.execute(ratg)
        data=cur.fetchall()
        print('THE MOVIES ARE AS FOLLOWS')
        for row in data:
            print(row[0]) 
        mycon.commit()
    if ch==5:
        sis=input("ENTER PRODUCER NAME TO SEARCH-")
        indys='select movie from movie where Producer like "%{}%"'.format(sis)
        cur.execute(indys)
        data=cur.fetchall()
        print('THE MOVIES ARE AS FOLLOWS :')
        for row in data:
            print(row[0]) 
        mycon.commit()
# main program
while True:
    print("WELCOME TO OUR PROJECT")
    name=input("ENTER YOUR NAME-")
    if name=='admin' or name=='ADMIN':
        print("YOU ARE A ADMIN")
        ch=int(input("ENTER PASSWORD-"))
        if ch==0000:
             opt=int(input("1 TO ADD\n2 TO UPDATE\nENTER YOUR CHOICE-"))
             if opt==1:
                 add()
             elif opt==2:
                 update()
    else:
        print("YOU ARE NOT A ADMIN SO YOU HAVE ONLY ACCESS FOR SEARCHING\n")
        search()
    fc=input("DO YOU WANT TO CONTINUE(Y/N)-")
    if fc=='n' or fc=='N':
        break
