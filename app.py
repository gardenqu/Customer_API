from faker import Faker
from src.models import Customer,db
from src import create_app


customer_count=10





def main():
    """Main driver function"""
    app=create_app()
    app.app_context().push()
    db.drop_all()
    db.create_all()
    fake = Faker()
    last_customer=None
    for i in range(customer_count):
        last_customer=Customer(fake.first_name(),fake.last_name(),fake.email(),fake.street_address(),fake.state_abbr(),fake.state_abbr(),fake.zipcode())
        db.session.add(last_customer)


    db.session.commit()

main()

