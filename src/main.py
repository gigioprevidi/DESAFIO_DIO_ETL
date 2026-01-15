from extract import extract_users
from transform import enrich_users
from load import load_users

def main():
    users = extract_users()
    users = enrich_users(users)
    load_users(users)

if __name__ == "__main__":
    main()
