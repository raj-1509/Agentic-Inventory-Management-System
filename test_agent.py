from app.agent import run_agent
from app.db import init_db
from app.vector_store import init_vector_db

init_db()
init_vector_db()

print("---- TEST 1 ----")
print(run_agent("Check stock of laptop"))

print("---- TEST 2 ----")
print(run_agent("Update laptop to 2"))

print("---- TEST 3 ----")
print(run_agent("Which items are low stock?"))

print("---- TEST 4 ----")
print(run_agent("Do we have 220V power supply?"))

print("---- TEST 5 ----")
print(run_agent("Show items with price greater than 1000"))