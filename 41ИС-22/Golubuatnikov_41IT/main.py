from teplovoz import Teplovoz
from vagon import Vagon
from sostav import Sostav

def main():
    teplovoz = Teplovoz("Т100", 1600)
    vagon1 = Vagon("В1", 50)
    vagon2 = Vagon("В2", 75)

    sostav = Sostav(teplovoz)
    sostav.add_vagon(vagon1)
    sostav.add_vagon(vagon2)

    # Запись информации о составе в файл
    sostav.write_to_file('sostavv_info.txt')

if __name__ == '__main__':
    main()