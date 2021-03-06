# coding: utf8
def index():
    books = db(db.t_book.id > 0).select()
    return dict(books=books)

def book():
    book = db(db.t_book.id == request.vars.book).select().first()
    chapters = db(db.t_chapter.f_book == request.vars.book).select()
    return dict(book = book, chapters = chapters)

from pyquery import PyQuery as pq
def chapter():
    chapter = db(db.t_chapter.id == request.vars.chapter).select().first()
    book_characters = db(db.t_character.f_book == chapter.f_book).select()
    # book_characters = db(db.t_character.id > 0).select()
    chapter_characters = db(db.t_character_reference.f_chapter == chapter).select()
    text = pq(chapter.f_text)
    text('p').map(lambda i, e: pq(e).prepend("&para; " + str(i+1) + ": "))
    text('p').map(lambda i, e: pq(e).attr('id',str(i+1)))
    questions = db(db.t_question.f_chapter == request.vars.chapter).select()
    answers = db(db.t_question.id > 0).select(db.t_question.f_answer)
    form = SQLFORM.factory(Field('choose_character','reference f_character')) 
    return dict(chapter = chapter, book = chapter.f_book, text = str(text), book_characters = book_characters, chapter_characters = chapter_characters,
                questions = questions, answers = answers, form = form)

def addquestion():
    chapter = request.vars.ques_chapter
    prompt = request.vars.ques_prompt
    paragraphs = request.vars.ques_paragraphs
    correct_answer = request.vars.ques_answer
    db.t_question.insert(f_chapter = chapter, f_prompt = prompt, f_paragraphs = paragraphs, f_answer = correct_answer)
    answers = db(db.t_question.f_chapter == chapter).select()    
    options = '<option value="">Choose An Answer</option>'
    for answer in answers:
        options += "<option value='%s'>%s</option>" % (answer.f_answer, answer.f_answer)
    new_question = '<li>%s<input type="hidden" id="correct_answer" value = "%s"/><select id="user_answer" name="user_answer">%s</select><button id="check_answer">Check Answer</button>><div id="correct" class="results" style="visibility: hidden">Correct</div><div id="incorrect" class="results" style="visibility: hidden">Incorrect</div></li>       <button class="show_refs">References</button><input id="paras" name="paras" type="hidden" value="%s"/>' % (prompt, correct_answer, options, paragraphs)
    # new_question = '<li>' + prompt + '<input type="hidden" id="correct_answer" value="' + answer + '"/><input id="user_answer"/><button id="check_answer">Check Answer</button><div id="correct" class="results" style="visibility: hidden">Correct</div><div id="incorrect" class="results" style="visibility: hidden">Incorrect</div></li>'
    return "$('#question_list').append('%s'); $('.ques_input').val(''); $('#frm_new_question').hide();  " % new_question

def editquestion():
    chapter = request.vars.ques_chapter
    prompt = request.vars.ques_prompt
    paragraphs = request.vars.ques_paragraphs
    answer = request.vars.ques_answer
    return "alert(%s)" % answer

def addcharacter():
    chapter = request.vars.char_chapter
    book = request.vars.char_book
    gender = request.vars.char_gender
    name = request.vars.char_name
    age = request.vars.char_age
    birthplace = request.vars.char_birthplace
    profession = request.vars.char_profession
    relations = request.vars.char_relations
    notes = request.vars.char_notes    
    character = db.t_character.insert(f_book = book, f_gender = gender, f_name = name, f_age = age, f_birthplace = birthplace, f_profession = profession, f_relations = relations, f_notes = notes)
    db.t_character_reference.insert(f_character = character, f_chapter = chapter)
    new_character = "<li><div>Name : %s</div><div>Gender : %s</div><div>Age : %s</div><div>Birthplace : %s</div><div>Profession : %s</div><div>Relations : %s</div><div>Notes : %s</div></li>" % (name, gender, age, birthplace, profession, relations, notes)
    new_character_short = "<li><div>Name : %s</div></li>" % name
    return "$('#book_character_list').append('%s'); $('#chapter_character_list').append('%s'); $('.character_input').val(''); $('#frm_new_character').hide(); " % (new_character, new_character_short)

def addcharacterreference():
    chapter = request.vars.ref_chapter
    character = request.vars.ref_character
    name = db(db.t_character.id == request.vars.ref_character).select().first().f_name
    db.t_character_reference.insert(f_character = character, f_chapter = chapter)
    new_character_short = "<li><div>Name : %s</div></li>" % name
    return "$('#chapter_character_list').append('%s'); $('#frm_new_character_reference').hide(); " % (new_character_short)
