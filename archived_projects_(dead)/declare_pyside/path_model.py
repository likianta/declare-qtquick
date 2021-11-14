from os.path import dirname

curr_dir = dirname(__file__).replace('\\', '/')
pkg_dir = curr_dir
proj_dir = dirname(pkg_dir)

qmlside_dir = f'{pkg_dir}/qmlside'
theme_dir = f'{pkg_dir}/theme'
widgets_dir = f'{pkg_dir}/widgets'

light_clean_theme_dir = f'{theme_dir}/LightClean'

lk_qml_side_dir = f'{qmlside_dir}/LKQmlSide'