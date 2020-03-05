from app.file_handling import store_pickle_file


def get_angle(query):
    return input(query)


def coronal_component():
    return get_angle('coronal component C (degrees): ')


def sagittal_component():
    return get_angle('sagittal component S (degrees): ')


def torsion_component():
    return get_angle('torsion component T (degrees): ')


def get_angles():
    input_angles = {
        "C": coronal_component(),
        "S": sagittal_component(),
        "T": torsion_component()
    }
    return input_angles


if __name__ == '__main__':
    angles = get_angles()
    store_pickle_file(angles, "pickle/angles.pkl")
    print(f"\tC = {angles['C']}°\n\tS = {angles['S']}°\n\tT = {angles['T']}°")
