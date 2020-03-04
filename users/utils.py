from datetime import datetime, timedelta


def age_to_dob(age):
    return (datetime.utcnow() - timedelta(days=age*365.3)).date()


def dob_to_age(dob):
    return round(int((datetime.utcnow().date() - dob) / timedelta(days=365.245)))
