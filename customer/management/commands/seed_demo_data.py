import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

from customer.models import Customer
from vehicles.models import Vehicle
from mechanics.models import Mechanic
from service.models import Service
from spareparts.models import SparePart
from invoice.models import Invoice

class Command(BaseCommand):
    help = 'Seeds the database with realistic demo data for testing and UI presentation'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting to seed demo data...")

        # 1. Customers
        customer_data = [
            {"name": "Kamal Perera", "phone": "0771234567", "email": "kamal@example.com", "address": "No 10, Galle Rd, Colombo 3"},
            {"name": "A. Razak", "phone": "0712345678", "email": "razak@example.com", "address": "15, Kandy Rd, Kadawatha"},
            {"name": "N. Silva", "phone": "0763456789", "email": "silva.n@example.com", "address": "22, High Level Rd, Nugegoda"},
            {"name": "S. Fernando", "phone": "0704567890", "email": "fernando.s@example.com", "address": "5/A, Negombo Rd, Wattala"},
            {"name": "M. Ibrahim", "phone": "0755678901", "email": "ibrahim.m@example.com", "address": "12, Maligawatta, Colombo 10"},
            {"name": "R. Kumar", "phone": "0776789012", "email": "kumar.r@example.com", "address": "8, Station Rd, Wellawatte"},
            {"name": "D. Perera", "phone": "0717890123", "email": "perera.d@example.com", "address": "18, Nawala Rd, Rajagiriya"},
            {"name": "F. Ahamed", "phone": "0768901234", "email": "ahamed.f@example.com", "address": "45, Havelock Rd, Colombo 5"},
            {"name": "T. Jayasinghe", "phone": "0709012345", "email": "jaya.t@example.com", "address": "33, Kotte Rd, Pitakotte"},
            {"name": "H. Mohamed", "phone": "0750123456", "email": "mohamed.h@example.com", "address": "27, Baseline Rd, Dematagoda"},
            {"name": "C. Silva", "phone": "0771122334", "email": "csilva@example.com", "address": "11, Beach Rd, Mount Lavinia"},
            {"name": "W. Bandara", "phone": "0712233445", "email": "bandara.w@example.com", "address": "9, Temple Rd, Maharagama"}
        ]

        customers_created = 0
        customers = []
        for c in customer_data:
            customer, created = Customer.objects.get_or_create(phone=c["phone"], defaults=c)
            if created:
                customers_created += 1
            customers.append(customer)

        self.stdout.write(f"Created {customers_created} customers.")

        # 2. Vehicles
        vehicle_data = [
            {"vehicle_number": "CBE-1234", "brand": "Toyota", "model": "Corolla", "year": 2018, "vehicle_type": "CAR", "current_mileage": 45000},
            {"vehicle_number": "CAW-5678", "brand": "Honda", "model": "Vezel", "year": 2016, "vehicle_type": "SUV", "current_mileage": 60000},
            {"vehicle_number": "BAM-9012", "brand": "Suzuki", "model": "Alto", "year": 2015, "vehicle_type": "CAR", "current_mileage": 85000},
            {"vehicle_number": "CAB-3456", "brand": "Toyota", "model": "Aqua", "year": 2014, "vehicle_type": "CAR", "current_mileage": 72000},
            {"vehicle_number": "KV-7890", "brand": "Nissan", "model": "March", "year": 2010, "vehicle_type": "CAR", "current_mileage": 110000},
            {"vehicle_number": "CAQ-2345", "brand": "Toyota", "model": "Prius", "year": 2017, "vehicle_type": "CAR", "current_mileage": 55000},
            {"vehicle_number": "CBG-6789", "brand": "Honda", "model": "Fit", "year": 2019, "vehicle_type": "CAR", "current_mileage": 35000},
            {"vehicle_number": "CBA-1234", "brand": "Suzuki", "model": "Wagon R", "year": 2017, "vehicle_type": "CAR", "current_mileage": 62000},
            {"vehicle_number": "CAT-5678", "brand": "Toyota", "model": "Axio", "year": 2015, "vehicle_type": "CAR", "current_mileage": 80000},
            {"vehicle_number": "CBK-9012", "brand": "Perodua", "model": "Axia", "year": 2020, "vehicle_type": "CAR", "current_mileage": 25000},
            {"vehicle_number": "KQ-3456", "brand": "Mitsubishi", "model": "Lancer", "year": 2008, "vehicle_type": "CAR", "current_mileage": 140000},
            {"vehicle_number": "HN-7890", "brand": "Nissan", "model": "Sunny", "year": 2005, "vehicle_type": "CAR", "current_mileage": 180000},
        ]

        vehicles_created = 0
        vehicles = []
        for i, v in enumerate(vehicle_data):
            customer = customers[i]
            # Since Customer has a OneToOne with Vehicle, check if customer already has a vehicle
            try:
                existing_vehicle = customer.vehicles
                vehicles.append(existing_vehicle)
            except Vehicle.DoesNotExist:
                vehicle, created = Vehicle.objects.get_or_create(vehicle_number=v["vehicle_number"], defaults={**v, "customer": customer})
                if created:
                    vehicles_created += 1
                vehicles.append(vehicle)

        self.stdout.write(f"Created {vehicles_created} vehicles.")

        # 3. Mechanics
        mechanic_data = [
            {"name": "Kasun", "phone": "0770011223", "specialization": "Engine Repair, General Service", "is_available": True},
            {"name": "Nimal", "phone": "0710022334", "specialization": "Electrical Repair, AC Repair", "is_available": True},
            {"name": "Rizwan", "phone": "0760033445", "specialization": "Body Wash, Interior Cleaning", "is_available": True},
            {"name": "Sahan", "phone": "0700044556", "specialization": "Brake Service, Suspension", "is_available": False},
            {"name": "Fawzan", "phone": "0750055667", "specialization": "Tire Service, Alignment", "is_available": True},
        ]

        mechanics_created = 0
        mechanics = []
        for m in mechanic_data:
            mechanic, created = Mechanic.objects.get_or_create(phone=m["phone"], defaults=m)
            if created:
                mechanics_created += 1
            mechanics.append(mechanic)

        self.stdout.write(f"Created {mechanics_created} mechanics.")

        # 4. Spare Parts
        spare_parts_data = [
            {"name": "Brake Pad (Toyota)", "category": "Brakes", "supplier": "AutoParts LK", "quantity": 6, "minimum_stock": 10, "unit_price": Decimal("4500.00")},
            {"name": "Engine Oil 10W-30", "category": "Oils & Fluids", "supplier": "Lube Traders", "quantity": 25, "minimum_stock": 15, "unit_price": Decimal("6500.00")},
            {"name": "Oil Filter (Universal)", "category": "Filters", "supplier": "FilterMasters", "quantity": 4, "minimum_stock": 8, "unit_price": Decimal("1200.00")},
            {"name": "Air Filter (Honda)", "category": "Filters", "supplier": "AutoParts LK", "quantity": 12, "minimum_stock": 5, "unit_price": Decimal("2500.00")},
            {"name": "Spark Plug (Denso)", "category": "Engine", "supplier": "ElectroAuto", "quantity": 40, "minimum_stock": 20, "unit_price": Decimal("850.00")},
            {"name": "Coolant (Red)", "category": "Oils & Fluids", "supplier": "Lube Traders", "quantity": 18, "minimum_stock": 10, "unit_price": Decimal("1500.00")},
            {"name": "Brake Fluid DOT4", "category": "Oils & Fluids", "supplier": "Lube Traders", "quantity": 8, "minimum_stock": 5, "unit_price": Decimal("900.00")},
            {"name": "Car Battery 45Ah", "category": "Electrical", "supplier": "BatteryWorld", "quantity": 3, "minimum_stock": 5, "unit_price": Decimal("18500.00")},
            {"name": "Wiper Blade 22 inch", "category": "Accessories", "supplier": "AutoParts LK", "quantity": 15, "minimum_stock": 10, "unit_price": Decimal("1100.00")},
            {"name": "Gear Oil 80W-90", "category": "Oils & Fluids", "supplier": "Lube Traders", "quantity": 10, "minimum_stock": 8, "unit_price": Decimal("3200.00")},
            {"name": "Radiator Hose (Upper)", "category": "Cooling", "supplier": "AutoParts LK", "quantity": 5, "minimum_stock": 5, "unit_price": Decimal("1800.00")},
            {"name": "Fan Belt", "category": "Engine", "supplier": "AutoParts LK", "quantity": 7, "minimum_stock": 10, "unit_price": Decimal("2200.00")},
        ]

        spare_parts_created = 0
        for sp in spare_parts_data:
            part, created = SparePart.objects.get_or_create(name=sp["name"], defaults=sp)
            if created:
                spare_parts_created += 1

        self.stdout.write(f"Created {spare_parts_created} spare parts.")

        # 5. Services & 6. Invoices
        service_types = [
            "Full Service", "Oil Change", "Brake Service", 
            "Engine Repair", "Body Wash", "Electrical Repair", 
            "AC Repair", "Tire Service"
        ]

        # Check if we already have services to avoid duplication
        if Service.objects.count() < 15:
            services_created = 0
            invoices_created = 0

            # Create ~20 services
            now = timezone.now()
            
            for i in range(20):
                vehicle = random.choice(vehicles)
                mechanic = random.choice(mechanics)
                service_type = random.choice(service_types)
                
                # Distribution of dates: some recent, some older, some future
                days_offset = random.randint(-45, 2)
                service_date = now + timedelta(days=days_offset)
                
                # Status distribution based on date
                if days_offset > 0:
                    status = Service.Status.PENDING
                elif days_offset > -2:
                    status = Service.Status.IN_PROGRESS
                elif random.random() < 0.1:
                    status = Service.Status.CANCELLED
                else:
                    status = Service.Status.COMPLETED

                estimated_cost = Decimal(random.randint(2500, 25000))
                actual_cost = estimated_cost if status == Service.Status.COMPLETED else None

                service = Service.objects.create(
                    vehicle=vehicle,
                    mechanic=mechanic,
                    service_date=service_date,
                    service_type=service_type,
                    problem_description=f"Customer reported issues related to {service_type.lower()}.",
                    mileage_at_service=vehicle.current_mileage - random.randint(100, 5000),
                    status=status,
                    estimated_cost=estimated_cost,
                    actual_cost=actual_cost,
                    notes="Demo service record."
                )
                services_created += 1

                # 6. Invoices for COMPLETED services
                if status == Service.Status.COMPLETED:
                    service_charge = actual_cost * Decimal('0.6')
                    parts_cost = actual_cost * Decimal('0.4')
                    discount = Decimal('0.00')
                    
                    payment_status_choice = random.choice([
                        Invoice.PaymentStatus.PAID, 
                        Invoice.PaymentStatus.PAID, 
                        Invoice.PaymentStatus.PARTIALLY_PAID, 
                        Invoice.PaymentStatus.PENDING
                    ])
                    
                    if payment_status_choice == Invoice.PaymentStatus.PAID:
                        paid_amount = actual_cost
                        payment_method = random.choice([Invoice.PaymentMethod.CASH, Invoice.PaymentMethod.CARD])
                    elif payment_status_choice == Invoice.PaymentStatus.PARTIALLY_PAID:
                        paid_amount = actual_cost / 2
                        payment_method = Invoice.PaymentMethod.CASH
                    else:
                        paid_amount = Decimal('0.00')
                        payment_method = None

                    Invoice.objects.create(
                        service=service,
                        invoice_date=service_date + timedelta(hours=random.randint(1, 48)),
                        service_charge=service_charge,
                        parts_cost=parts_cost,
                        discount=discount,
                        paid_amount=paid_amount,
                        payment_status=payment_status_choice,
                        payment_method=payment_method,
                        notes="Demo invoice."
                    )
                    invoices_created += 1

            self.stdout.write(f"Created {services_created} services.")
            self.stdout.write(f"Created {invoices_created} invoices.")
        else:
            self.stdout.write("Services and Invoices already exist, skipping to avoid duplicates.")

        self.stdout.write(self.style.SUCCESS('Successfully seeded demo data!'))
