{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "eee49895-aa67-45aa-8416-c6799e8647c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "accounts = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "0c3780c0-c67c-4a9e-ab9f-c2aab490c122",
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_account(account_number, name, initial_balance=0):\n",
    "    if account_number in accounts:\n",
    "        print(\"Account already exists\")\n",
    "        return\n",
    "    if initial_balance < 0:\n",
    "        print(\"Initial balance cannot be negative\")\n",
    "        return\n",
    "    accounts[account_number] = {\n",
    "        \"name\": name,\n",
    "        \"balance\": initial_balance,\n",
    "        \"transactions\": []\n",
    "    }\n",
    "    print(f\"Account created for {name}\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "f679f24e-a006-4623-8783-45035bf28c8b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Account already exists\n",
      "Account created for Sarwar\n"
     ]
    }
   ],
   "source": [
    "create_account(123,\"muhammad\")\n",
    "create_account(124,\"Sarwar\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "f82632fa-955d-4c6a-9421-807586102d6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def deposit(account_number, amount):\n",
    "    if account_number not in accounts:\n",
    "        print(\"Account does not exist\")\n",
    "        return\n",
    "    if amount <= 0:\n",
    "        print(\"Deposit amount must be positive\")\n",
    "        return\n",
    "    accounts[account_number][\"balance\"] += amount\n",
    "    transaction = f\"Deposited: {amount}\"\n",
    "    accounts[account_number][\"transactions\"].append(transaction)\n",
    "    try:\n",
    "        with open(f\"{account_number}_transactions.txt\", \"a\") as file:\n",
    "            file.write(transaction + \"\\n\")\n",
    "    except IOError:\n",
    "        print(\"An error occurred while writing the transaction to the file.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "83f3c38e-62e0-450b-9cc0-dec95cbe71c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "deposit(123,5000)\n",
    "deposit(124,10000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "25708118-d492-492a-8242-8520289700fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def withdraw(account_number, amount):\n",
    "    if account_number not in accounts:\n",
    "        print(\"Account does not exist\")\n",
    "        return\n",
    "    if amount <= 0:\n",
    "        print(\"Withdrawal amount must be positive\")\n",
    "        return\n",
    "    if accounts[account_number][\"balance\"] < amount:\n",
    "        print(\"Insufficient balance\")\n",
    "        return\n",
    "    accounts[account_number][\"balance\"] -= amount\n",
    "    transaction = f\"Withdrew: {amount}\"\n",
    "    accounts[account_number][\"transactions\"].append(transaction)\n",
    "    try:\n",
    "        with open(f\"{account_number}_transactions.txt\", \"a\") as file:\n",
    "            file.write(transaction + \"\\n\")\n",
    "    except IOError:\n",
    "        print(\"An error occurred while writing the transaction to the file.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "b3a1144e-2745-4c2f-b0ab-b8b08f0ddcf8",
   "metadata": {},
   "outputs": [],
   "source": [
    "withdraw(123,2000)\n",
    "withdraw(124,3000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "4f4452b8-d004-4aed-901c-89722340ebeb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_balance(account_number):\n",
    "    if account_number not in accounts:\n",
    "        print(\"Account does not exist\")\n",
    "        return\n",
    "    print(f\"Current balance for account {account_number}: {accounts[account_number]['balance']}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "96557c5f-6aeb-48ee-a080-8c644970d8dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current balance for account 123: 6000\n",
      "Current balance for account 124: 7000\n"
     ]
    }
   ],
   "source": [
    "check_balance(123)\n",
    "check_balance(124)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "77f3011f-d923-4ce8-b38c-39ce3d4d1598",
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_statement(account_number):\n",
    "    if account_number not in accounts:\n",
    "        print(\"Account does not exist\")\n",
    "        return\n",
    "    transactions = accounts[account_number][\"transactions\"]\n",
    "    if not transactions:\n",
    "        print(\"No transactions found\")\n",
    "        return\n",
    "    print(f\"Transaction history for account {account_number}:\")\n",
    "    for transaction in transactions:\n",
    "        print(transaction)\n",
    "    print(f\"Current balance: {accounts[account_number]['balance']}\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "a57786fb-f7da-4d92-9adf-3315298c353f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Transaction history for account 123:\n",
      "Deposited: 5000\n",
      "Withdrew: 2000\n",
      "Deposited: 5000\n",
      "Withdrew: 2000\n",
      "Current balance: 6000\n",
      "Transaction history for account 124:\n",
      "Deposited: 10000\n",
      "Withdrew: 3000\n",
      "Current balance: 7000\n"
     ]
    }
   ],
   "source": [
    "print_statement(123)\n",
    "print_statement(124)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4895cd00-855d-49d3-9587-e8857cd0c680",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
