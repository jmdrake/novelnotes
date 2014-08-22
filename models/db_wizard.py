### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_book',
    Field('f_title', type='string',
          label=T('Title')),
    Field('f_author', type='string',
          label=T('Author')),
    auth.signature,
    format='%(f_title)s',
    migrate=settings.migrate)

db.define_table('t_book_archive',db.t_book,Field('current_record','reference t_book',readable=False,writable=False))

########################################
db.define_table('t_chapter',
    Field('f_number', type='integer',
          label=T('Number')),
    Field('f_title', type='string',
          label=T('Title')),
    Field('f_book', type='reference t_book',
          label=T('Book')),
    Field('f_text', type='text',
          label=T('Text')),
    auth.signature,
    format='%(f_title)s',
    migrate=settings.migrate)

db.define_table('t_chapter_archive',db.t_chapter,Field('current_record','reference t_chapter',readable=False,writable=False))

########################################
db.define_table('t_question',
    Field('f_chapter', type='reference t_chapter',
          label=T('Chapter')),
    Field('f_paragraphs', type='string',
          label=T('Paragraphs Containing Answer')),
    Field('f_prompt', type='string',
          label=T('Prompt')),
    Field('f_answer', type='string',
          label=T('Answer')),
    auth.signature,
    format='%(f_prompt)s',
    migrate=settings.migrate)

db.define_table('t_question_archive',db.t_question,Field('current_record','reference t_question',readable=False,writable=False))

########################################
db.define_table('t_character',
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_gender', type='string',
          label=T('Gender')),
    Field('f_age', type='string',
          label=T('Age')),
    Field('f_birthplace', type='string',
          label=T('Place Of Birth')),
    Field('f_relations', type='text',
          label=T('Relations')),
    Field('f_profession', type='text',
          label=T('Profession')),
    Field('f_notes', type='text',
          label=T('Notes')),
    Field('f_book', type='reference t_book',
          label=T('Book')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_character_archive',db.t_character,Field('current_record','reference t_character',readable=False,writable=False))

########################################
db.define_table('t_character_reference',
    Field('f_character', type='reference t_character',
          label=T('Character')),
    Field('f_chapter', type='reference t_chapter',
          label=T('Chapter')),
    auth.signature,
    format='%(f_character)s',
    migrate=settings.migrate)

db.define_table('t_character_reference_archive',db.t_character_reference,Field('current_record','reference t_character_reference',readable=False,writable=False))

db.define_table('t_illustration',
    Field('f_description', type='string',
          label=T('Description')),
    Field('f_image', type='upload',
          label=T('Image')),
    Field('f_chapter', type='reference t_chapter',
          label=T('Chapter')),
    Field('f_paragraph', type='integer',
          label=T('Paragraph')),
    auth.signature,
    format='%(f_description)s',
    migrate=settings.migrate)

db.define_table('t_illustration_archive',db.t_character_reference,Field('current_record','reference t_illustration',readable=False,writable=False))
