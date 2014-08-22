# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

@auth.requires_login()
def book_manage():
    form = SQLFORM.smartgrid(db.t_book,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def chapter_manage():
    form = SQLFORM.smartgrid(db.t_chapter,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def character_manage():
    form = SQLFORM.smartgrid(db.t_character,onupdate=auth.archive)
    characters = db(db.t_character.id > 0).select()
    return locals()

@auth.requires_login()
def character_reference_manage():
    form = SQLFORM.smartgrid(db.t_character_reference,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def question_manage():
    form = SQLFORM.smartgrid(db.t_question,onupdate=auth.archive)
    return locals()
