# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()



@auth.requires_login()
@auth.requires_membership('user_1')
def createstudent():
   form = SQLFORM(db.student_info)
   if form.process().accepted:
        response.flash="Student created"   
   return dict(form=form)

@auth.requires_membership('user_1')
def show1():
     response.flash = T("Welcome")
     return dict(message=T('Welcome to web2py!'))


@auth.requires_membership('user_1')
def createSub_taken():
   form = SQLFORM(db.Sub_taken)
   if form.process().accepted:
        response.flash="Sub_taken  created"
   return dict(form=form)
@auth.requires_membership('user_1')
def createISSUE():
   form = SQLFORM(db.ISSUE)
   if form.process().accepted:
        response.flash="ISSUE  created"
   return dict(form=form)
@auth.requires_membership('user_1')
def createSubject():
   form = SQLFORM(db.Subject)
   if form.process().accepted:
        response.flash="Subject  created"
   return dict(form=form)
@auth.requires_membership('user_1')
def createBook_acc():
   form = SQLFORM(db.Book_acc)
   if form.process().accepted:
        response.flash="Book_acc  created"
   return dict(form=form)
@auth.requires_membership('user_1')
def createBooks():
   form = SQLFORM(db.Books)
   if form.process().accepted:
        response.flash="Books  created"
   return dict(form=form)
@auth.requires_membership('user_1')
def register():
    form=SQLFORM.factory(db.Books,db.Book_acc,db.student_info,db.Subject,db.Sub_taken,db.ISSUE)
    if form.process().accepted:
        response.flash='Thanks for filling the form'
    return dict(form=form)
@auth.requires_membership('user_1')
def display_form():
   Search=FORM('Enter name:', INPUT(_name='name'), INPUT(_type='submit'))
   rows=db(db.student_info.F_name==(request.vars.name)).select(db.student_info.ALL)
   return locals()


@auth.requires_membership('user_1')
def display_form2():
   Search=FORM('Enter UID:', INPUT(_name='name'), INPUT(_type='submit'))
   rows=db(db.student_info.u_id==(request.vars.name)).select(db.student_info.ALL)
   SearchName=FORM('Enter Name:', INPUT(_name='name1'), INPUT(_type='submit'))
   rows1=db(db.student_info.F_name==(request.vars.name1)).select(db.student_info.ALL)
   return locals()

@auth.requires_membership('user_1')
def display_form3():
    Search=FORM('Enter UID:', INPUT(_name='name'), INPUT(_type='submit'))
    Books=db(db.ISSUE.u_id==(request.vars.name)).select(db.ISSUE.ALL)
    Student=db(db.student_info.u_id==(request.vars.name)).select(db.student_info.ALL)
    Return=FORM('Enter UID:', INPUT(_name='name3'), 'Enter Acc:', INPUT(_name='name1'), '  Enter Return Date(yyyy/mm/dd):', INPUT(_name='name2'), INPUT(_type='submit'))
    db(db.ISSUE.Acc_no==(request.vars.name1))(db.ISSUE.u_id==(request.vars.name3)).update(Return_date=(request.vars.name2))
    #OB.update_record(Return_date=(request.vars.return_date))
    #db(db[tablename]._id==id).update(**{fieldname:value})
    #OB.update_record(Return_date=(request.vars.return_date))
    #row = db(db.ISSUE.Acc_no==(request.vars.acc))
    #row.update(Return_date=(request.vars.return_date))
    return locals()


@auth.requires_membership('user_1')
def display_books():
    Search=FORM('Enter Book ID:', INPUT(_name='name'), INPUT(_type='submit'))
    Books=db(db.Books.Book_id==(request.vars.name)).select(db.Books.ALL)
    call=db(db.Book_acc.Book_id==(request.vars.name)).select(db.Book_acc.Book_id,db.Book_acc.Acc_no,db.Book_acc.call_no)
    return locals()
@auth.requires_membership('user_1')
def display_form4():
    Search=FORM('Enter UID:', INPUT(_name='name'), INPUT(_type='submit'))
    Books=db(db.ISSUE.u_id==(request.vars.name)).select(db.ISSUE.ALL)
    Return=FORM('Enter Acc No and return date:',INPUT(_name='AccNo'),INPUT(_name='Return'), INPUT(_type='submit'))
    return locals()


def update():
    Search=FORM('Enter UID:', INPUT(_name='name'), INPUT(_type='submit'))
    Books=db(db.ISSUE.u_id==(request.vars.name),readonly=True ).select(db.ISSUE.ALL)
    Return=FORM('Enter Acc No and return date:',INPUT(_name='AccNo'),INPUT(_name='Return'), INPUT(_type='submit'))
    return locals()



def build_form(readonly=False):
    #create fields or get from
    Search=FORM('Enter UID:', INPUT(_name='name'), INPUT(_type='submit'))
    field2=db.ISSUE.u_id
    field2.default='123'
    #give it to the
    form = SQLFORM.factory( *[field2], readonly=readonly )

def frm():
    Search=FORM('Enter UID:', INPUT(_name='name'), INPUT(_type='submit'))
    form=SQLFORM.smartgrid(db.ISSUE)
    return locals()

@auth.requires_membership('user_1')
def updateissue():
    form=SQLFORM.smartgrid(db.ISSUE)
    return locals()
@auth.requires_membership('user_1')
def updatestudent():
    form=SQLFORM.smartgrid(db.student_info)
    return locals()
@auth.requires_membership('user_1')
def updatebooks():
    form=SQLFORM.smartgrid(db.Books)
    return locals()
@auth.requires_membership('user_1')
def updateSubject():
    form=SQLFORM.smartgrid(db.Subject)
    return locals()
@auth.requires_membership('user_1')
def updatesubjecttaken():
    form=SQLFORM.smartgrid(db.Sub_taken)
    return locals()
@auth.requires_membership('user_1')
def list_users():
    btn = lambda row: A("Edit", _href=URL('manage_user', args=row.auth_user.id))
    db.auth_user.edit = Field.Virtual(btn)
    rows = db(db.auth_user).select()
    headers = ["ID", "Name", "Last Name", "Email", "Edit"]
    fields = ['id', 'first_name', 'last_name', "email", "edit"]
    table = TABLE(THEAD(TR(*[B(header) for header in headers])),
                  TBODY(*[TR(*[TD(row[field]) for field in fields]) \
                        for row in rows]))
    table["_class"] = "table table-striped table-bordered table-condensed"
    return dict(table=table)

@auth.requires_membership('user_1')
def manage_user():
    user_id = request.args(0) or redirect(URL('list_users'))
    form = SQLFORM(db.auth_user, user_id).process()
    membership_panel = LOAD(request.controller,
                            'manage_membership.html',
                             args=[user_id],
                             ajax=True)
    return dict(form=form,membership_panel=membership_panel)


@auth.requires_membership('user_1') 
def manage_membership():
    user_id = request.args(0) or redirect(URL('list_users'))
    db.auth_membership.user_id.default = int(user_id)
    db.auth_membership.user_id.writable = False
    form = SQLFORM.grid(db.auth_membership.user_id == user_id,
                       args=[user_id],
                       searchable=False,
                       deletable=False,
                       details=False,
                       selectable=False,
                       csv=False,
                       user_signature=False)
    return form
