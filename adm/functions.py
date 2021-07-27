def tira_acento(email):
    email = email.lower()
    """
    email = email.replace('Ç', 'C')
    email = email.replace('Á', 'A')
    email = email.replace('À', 'A')
    email = email.replace('Ã', 'A')
    email = email.replace('Â', 'A')
    email = email.replace('É', 'E')
    email = email.replace('Ê', 'E')
    email = email.replace('Í', 'I')
    email = email.replace('Ó', 'O')
    email = email.replace('Õ', 'O')
    email = email.replace('Ô', 'O')
    email = email.replace('Ú', 'U')
    """

    email = email.replace('ç', 'c')
    email = email.replace('á', 'a')
    email = email.replace('à', 'a')
    email = email.replace('ã', 'a')
    email = email.replace('â', 'a')
    email = email.replace('é', 'e')
    email = email.replace('ê', 'e')
    email = email.replace('í', 'i')
    email = email.replace('ó', 'o')
    email = email.replace('õ', 'o')
    email = email.replace('ô', 'o')
    email = email.replace('ú', 'u')

    return email
