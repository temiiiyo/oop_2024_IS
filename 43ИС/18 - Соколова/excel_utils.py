import pandas as pd

def save_to_excel(sostav, filename="sostav.xlsx"):
    data = []
    for vagon in sostav.vagons:
        for mesto in vagon.mesta:
            data.append({
                'Вагон': vagon.id,
                'Место': mesto.number,
                'Тип места': mesto.type,
                'Занято': mesto.occupied
            })
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Состав сохранен в {filename}")
