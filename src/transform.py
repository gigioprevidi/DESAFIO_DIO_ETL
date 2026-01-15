def generate_marketing_message(user_name):
    return (
        f"Olá, {user_name}! 👋\n\n"
        "Investir é uma decisão estratégica para quem deseja segurança financeira "
        "e crescimento ao longo do tempo.\n\n"
        "Conte com o Santander para investir melhor! 💰📈"
    )

def enrich_users(users):
    for user in users:
        user["news"].append({
            "title": "Invista no seu futuro",
            "description": generate_marketing_message(user["name"])
        })
    return users
