from datetime import date
from datetime import timedelta

from src.enums import Gender, EmploymentType
from src.users.agent import Agent
from src.users.manager import Manager
from src.branch.branch import Branch
from src.payment.concrete_factories import CreditCardPaymentCreator

branch1 = Branch(
    name="Main Branch",
    city="Copenhagen",
    address="123 Main St",
    phone_number="+45 12345678"
)

agent1= Agent(
    first_name="Peyman",
    last_name="Khodabandehlouei",
    gender=Gender.MALE,
    birth_date=date.today() - timedelta(days=365*25),
    email="itspeey@gmail.com",
    address="123 Main St.",
    phone_number="00905343940796",
    branch=branch1,
    is_active=True,
    salary=2000,
    hire_date=date.today(),
    employment_type=EmploymentType.FULL_TIME
)

payment_service = CreditCardPaymentCreator(
    card_number="4000000000000002",
    cvv="123",
    expiry="12/25"
)

receipt = payment_service.execute_payment(3000)
print(receipt)
