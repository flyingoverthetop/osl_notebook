from django.conf.urls.defaults import *
from django.contrib import databrowse
from django.views.generic import list_detail

from notebook.notes.models import Note, Tag



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


#databrowse.site.register(Note)
#databrowse.site.register(Tag)

urlpatterns = patterns('',
   
    (r'^notes/$','notebook.notes.views.index'),

    #TODO: if social app can use this to get tags too
    (r'getWsTags/','notebook.notes.views.get_ws_tags'),
    
    #(r'^notes/tags/$','notebook.notes.views.alltags'), #not used

    (r'^settings/folders/$', 'notebook.notes.views.settings_folders'),
    (r'^settings/folders/folder/(?P<folder_name>[^/]+)/$', 'notebook.notes.views.settings_folder'),
    (r'^settings/folders/folder/(?P<folder_name>[^/]+)/updateFolder/$', 'notebook.notes.views.settings_folder_update'),
    (r'^settings/folders/addFolder/$', 'notebook.notes.views.settings_folder_add'),

    #this below can also match url settings/tags/addTag/. But since it is put after setting's url patterns, it should be fine. TODO:better
    (r'^(?P<aspect_name>[^/]+)/tags/(?P<tag_name>[^/]+)/$','notebook.notes.views.tags'), #TODO:regex here

    (r'/updateNoteInline/$','notebook.notes.views.update_note_inline'), #TODO:maybe no / after updateNote   
    (r'/updateNoteTagsInline/$','notebook.notes.views.update_note_tags_inline'), 
    (r'/addNotesToFrame/$','notebook.notes.views.add_notes_to_frame'), 
    (r'/createNoteInFrame/$','notebook.notes.views.create_note_in_frame'), 


    (r'/addComment/$','notebook.notes.views.add_comment'),
    (r'/deleteComment/$','notebook.notes.views.delete_comment'),
    (r'/makePrivate/$','notebook.notes.views.make_private'),
    (r'/makePublic/$','notebook.notes.views.make_public'),


    (r'/voteUpNote/$','notebook.notes.views.vote_up_note'), 
    (r'/voteDownNote/$','notebook.notes.views.vote_down_note'),
    (r'/deleteNote/$','notebook.notes.views.delete_note'),
    (r'/discardNote/$','notebook.notes.views.discard_note'),
    (r'/restoreNote/$','notebook.notes.views.restore_note'),
    (r'/addNote/$','notebook.notes.views.add_note'),    
    (r'/linkNotes/$','notebook.notes.views.frame_notes'),  
    #(r'^frames/$','notebook.notes.views.frames'),
    (r'^frames/frame/(?P<frame_id>[^/]+)/$','notebook.notes.views.frame'),  
    (r'^linkagenotes/$','notebook.notes.views.linkagenotes'),
    (r'^linkagenotes/note/(?P<note_id>[^/]+)/$','notebook.notes.views.linkagenote'),
    #(r'/updateLinkageNoteInline/$','notebook.notes.views.update_frame_inline'),
    #(r'/deleteLinkage/$','notebook.notes.views.delete_frame'),
    (r'/deleteNoteFromFrame/$','notebook.notes.views.delete_note_from_frame'),    
    (r'/addTags2Notes/$','notebook.notes.views.add_tags_to_notes'),
    #(r'/removeTagsFromNotes/$','notebook.notes.views.remove_tags_from_notes'),

    (r'/addTags2Notes2/$','notebook.notes.views.add_tags_to_notes2'),
    (r'/removeTagsFromNotes2/$','notebook.notes.views.remove_tags_from_notes2'),

    (r'/saveSearch/$','notebook.notes.views.save_search'),

    (r'^folders/(?P<folder_name>[^/]*)/$','notebook.notes.views.folders'),
    (r'^folders/$','notebook.notes.views.folders_index'),

    (r'^caches/(?P<cache_id>[^/]+)/addNotes2Cache/$','notebook.notes.views.add_notes_to_cache'), 
    (r'^caches/(?P<cache_id>[^/]+)/clearCache/$','notebook.notes.views.clear_cache'), 
    #TODO:Might need to update the url for caches. It seems better to be r'^caches/cache/(?P<cache_id>[^/]+)/notes/$'
    (r'^caches/(?P<cache_id>[^/]+)/$','notebook.notes.views.caches'), 
    #below is only for after notebook/  . 
    (r'^frames/frame/(?P<frame_id>[^/]+)/notes/$','notebook.notes.views.included_notes_in_frame'), 
    (r'^linkages/linkage/(?P<linkage_id>[^/]+)/notes/$','notebook.notes.views.included_notes_in_linkage'), 

    (r'^notes/note/(?P<note_id>[^/]+)/$','notebook.notes.views.note'),
    (r'^notes/note_raw/(?P<note_id>[^/]+)/$','notebook.notes.views.note_raw'),
    
(r'^notes/note/(?P<note_id>[^/]+)/updateNote/$','notebook.notes.views.update_note'),
    (r'^notes/note/(?P<note_id>[^/]+)/updateNoteTrans/$','notebook.notes.views.update_note_trans'),
    (r'^linkagenotes/note/(?P<note_id>[^/]+)/updateLinkageNote/$','notebook.notes.views.update_linkagenote'),
    #below actually applied to framebook
    (r'^notes/note/(?P<note_id>[^/]+)/getRelatedFrames/$','notebook.notes.views.get_related_frames'),

    (r'^setNotesPrivate/$','notebook.notes.views.set_notes_private'),
    (r'^setNotesPublic/$','notebook.notes.views.set_notes_public'),

    (r'^notes/note/(?P<note_id>[^/]+)/setOrder/$','notebook.notes.views.set_notes_order_in_frame'),



 




)
