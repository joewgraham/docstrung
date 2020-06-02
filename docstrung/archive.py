from docstrung import get
from datetime import datetime
import os



def archive_package(package_name, archive_dir='auto', overwrite=False):
    """Archives the package directory.
    """

    print()
    print('docstrung.archive.archive_package')
    print('---------------------------------')

    date = datetime.today().strftime('%Y%m%d')

    package_location = get_package_location(package_name)

    if archive_dir == 'auto':
        archive_dir = os.path.join(package_location, package_name + '_' + date)
    elif archive_dir == 'docstrung':
        archive_dir = os.path.join(os.getcwd(), package_name + '_docstrung')

    file_index = 0
    while os.path.isdir(archive_dir):
        if overwrite:
            shutil.rmtree(archive_dir)
            print('Overwriting existing dir:', archive_dir)
        else:
            file_index += 1
            archive_dir += '_' + str(file_index)
    
    if not os.path.isdir(archive_dir):
        shutil.copytree(package_dir, archive_dir)
        print('Copied:', package_dir)
        print('    To:', archive_dir)
    else:
        print('Warning: Not overwriting existing dir:', archive_dir)

    print('---------------------------------')
    print()

    return archive_dir, package_dir



def restore_original(package_name, archive_dir):
    """Deletes the current package directory and replaces it with an archived copy.
    """

    print()
    print('docstrung.archive.restore_original')
    print('----------------------------------')

    print('Copying archive:', archive_dir)
    shutil.copytree(archive_dir, 'temp_dir')
    
    print('Removing package directory')
    package_location = get_package_location(package_name)
    shutil.rmtree(package_location)
    
    print('Restoring archive to:', package_location)
    shutil.copytree('temp_dir', package_location)
    shutil.rmtree('temp_dir')

    print('----------------------------------')
    print()


