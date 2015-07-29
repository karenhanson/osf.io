# encoding: utf-8

from framework.routing import Rule, json_renderer

from website.addons.osfstorage import views


api_routes = {

    'prefix': '/api/v1',

    'rules': [

        Rule(
            [
                '/project/<pid>/osfstorage/',
                '/project/<pid>/node/<nid>/osfstorage/',
                '/project/<pid>/osfstorage/<fid>/',
                '/project/<pid>/node/<nid>/osfstorage/<fid>/',
            ],
            'get',
            views.osfstorage_get_metadata,
            json_renderer,
        ),

        Rule(
            [
                '/project/<pid>/osfstorage/<fid>/',
                '/project/<pid>/node/<nid>/osfstorage/<fid>/',
            ],
            'delete',
            views.osfstorage_delete,
            json_renderer,
        ),

        Rule(
            [
                '/project/<pid>/osfstorage/<fid>/download/',
                '/project/<pid>/node/<nid>/osfstorage/<fid>/download/',
            ],
            'get',
            views.osfstorage_download,
            json_renderer,
        ),

        Rule(
            [
                '/project/<pid>/osfstorage/<fid>/revisions/',
                '/project/<pid>/node/<nid>/osfstorage/<fid>/revisions/',
            ],
            'get',
            views.osfstorage_get_revisions,
            json_renderer,
        ),

        Rule(
            [
                '/project/<pid>/osfstorage/<fid>/lineage/',
                '/project/<pid>/node/<nid>/osfstorage/<fid>/lineage/',
            ],
            'get',
            views.osfstorage_get_lineage,
            json_renderer,
        ),

        Rule(
            [
                '/project/<pid>/osfstorage/<fid>/children/',
                '/project/<pid>/node/<nid>/osfstorage/<fid>/children/',
            ],
            'post',
            views.osfstorage_create_child,
            json_renderer,
        ),

        Rule(
            [
                '/project/<pid>/osfstorage/<fid>/children/',
                '/project/<pid>/node/<nid>/osfstorage/<fid>/children/',
            ],
            'get',
            views.osfstorage_get_children,
            json_renderer,
        ),

        Rule(
            [
                '/project/<pid>/osfstorage/hooks/metadata/',
                '/project/<pid>/node/<nid>/osfstorage/hooks/metadata/',
            ],
            'put',
            views.osfstorage_update_metadata,
            json_renderer,
        ),

        Rule(
            [
                '/project/<pid>/osfstorage/hooks/move/',
                '/project/<pid>/node/<nid>/osfstorage/hooks/move',
            ],
            'post',
            views.osfstorage_move_hook,
            json_renderer,
        ),

        Rule(
            [
                '/project/<pid>/osfstorage/hooks/copy/',
                '/project/<pid>/node/<nid>/osfstorage/hooks/copy/',
            ],
            'post',
            views.osfstorage_copy_hook,
            json_renderer,
        ),

        Rule(
            [
                '/project/<nid>/osfstorage/<fid>/rent/',
            ],
            'post',
            views.osfstorage_rent,
            json_renderer,
        ),

        Rule(
            [
                '/project/<nid>/osfstorage/<fid>/return/',
            ],
            'post',
            views.osfstorage_return,
            json_renderer,
        ),

        Rule(
            [
                '/project/<nid>/osfstorage/<fid>/rented/',
            ],
            'get',
            views.osfstorage_rented,
            json_renderer,
        ),

        Rule(
            [
                '/project/<nid>/osfstorage/<fid>/force_return/',
            ],
            'post',
            views.osfstorage_force_return,
            json_renderer,
        ),

        Rule(
            [
                '/project/<nid>/osfstorage/rent_all/',
            ],
            'post',
            views.osfstorage_rent_all,
            json_renderer,
        ),

        Rule(
            [
                '/project/<nid>/osfstorage/return_all/',
            ],
            'post',
            views.osfstorage_return_all,
            json_renderer,
        ),

    ],

}
