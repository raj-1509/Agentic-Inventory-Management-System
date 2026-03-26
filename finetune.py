from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model

# -----------------------------
# 1. Load Dataset
# -----------------------------
dataset = load_dataset("json", data_files="data/train.json")

# -----------------------------
# 2. Load Model + Tokenizer
# -----------------------------
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_name)

# 🔥 IMPORTANT FIX (padding)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(model_name)

# -----------------------------
# 3. Apply LoRA
# -----------------------------
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)

# -----------------------------
# 4. Format Dataset
# -----------------------------
def format_data(example):
    text = f"Input: {example['input']}\nOutput: {example['output']}"

    tokens = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=128
    )

    # 🔥 IMPORTANT: labels required for loss
    tokens["labels"] = tokens["input_ids"].copy()

    return tokens


# Apply formatting
tokenized = dataset.map(format_data)

# -----------------------------
# 5. Training Arguments
# -----------------------------
training_args = TrainingArguments(
    output_dir="./finetuned_model",
    per_device_train_batch_size=2,
    num_train_epochs=3,
    logging_steps=1,
    save_strategy="epoch"
)

# -----------------------------
# 6. Trainer
# -----------------------------
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized["train"]
)

# -----------------------------
# 7. Train
# -----------------------------
trainer.train()

# -----------------------------
# 8. Save Model
# -----------------------------
model.save_pretrained("finetuned_model")
tokenizer.save_pretrained("finetuned_model")

print("✅ Fine-tuning completed and model saved!")