screen_size = (600,600)
tile_amount = (10,10)
spawn_cord = (1,1)
snake_speed = 2
fps = 60
snake_head_path = 'textures\\snake\\snake_head.png'
snake_tail_path = 'textures\\snake\\snake_tail.png'

tile_darker_path = 'textures\\tiles\\tile_darker.png'
tile_lighter_path = 'textures\\tiles\\tile_lighter.png'
tile_border_path = 'textures\\tiles\\tile_border.png'

upgrade_path = 'textures\\upgrade\\apple.png'

shit_path = 'textures\\shit\\shit.png'

tile_map_dict = { 0: tile_darker_path,
                  1: tile_lighter_path }
real_tile_amount = (tile_amount[0] + 2, tile_amount[1] + 2)
tile_size = (screen_size[0] // real_tile_amount[0], screen_size[1] // real_tile_amount[1])