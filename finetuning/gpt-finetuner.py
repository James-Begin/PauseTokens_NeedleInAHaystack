from openai import OpenAI
client = OpenAI()

job = client.fine_tuning.jobs.create(
    training_file="gpt-data",
    model="gpt-4o-2024-08-06",
    method={
        "type": "dpo",
        "dpo": {
            "hyperparameters": {"beta": 0.1},
        },
    },
)

client.fine_tuning.jobs.create(
    training_file="gpt-data",
    model="gpt-4o-mini-2024-07-18"
)