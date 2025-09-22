import re
from typing import List, Optional, Dict, Any
from datetime import datetime
from dataclasses import dataclass, asdict
import jdatetime
from pprint import PrettyPrinter


@dataclass
class Stats:
    """Employee statistics tracking working and employment status."""
    working: bool = False
    employed: bool = False
    hire_date: Optional[str] = None
    last_status_change: Optional[str] = None

    def _update_working(self, working: bool):
        """Update working status with timestamp."""
        self.working = working
        self.last_status_change = jdatetime.datetime.now().isoformat()

    def _update_employed(self, employed: bool):
        """Update employment status with timestamp."""
        self.employed = employed
        if employed and not self.hire_date:
            self.hire_date = jdatetime.datetime.now().isoformat()
        self.last_status_change = jdatetime.datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        """Convert stats to dictionary format."""
        return asdict(self)


class Person:
    """Represents a person with validated personal information."""

    def __init__(self, name: str, birth_date: str, national_id: str, phone_number: str, email: str):
        self.name = self._validate_name(name)
        self.birth_date = self._validate_birth_date(birth_date)
        self.national_id = self._validate_national_id(national_id)
        self.phone_number = self._validate_phone_number(phone_number)
        self.email = self._validate_email(email)
        self.stats = Stats()
        self.created_at = jdatetime.datetime.now().isoformat()

    def _validate_name(self, name: str) -> str:
        if not name or len(name.strip()) < 2:
            raise ValueError("Name must be at least 2 characters long.")
        return name.strip()

    def _validate_birth_date(self, birth_date: str) -> jdatetime.date:
        # Accepts "YYYY/M/D" or "YYYY/MM/DD"
        try:
            parts = [int(p) for p in birth_date.strip().split('/')]
            if len(parts) != 3:
                raise ValueError
            bd = jdatetime.date(parts[0], parts[1], parts[2])
            # Optional: check reasonable age range (18-65 years old)
            today = jdatetime.date.today()
            age = today.year - bd.year - ((today.month, today.day) < (bd.month, bd.day))
            if not (18 <= age <= 65):
                raise ValueError("Age must be between 18 and 65.")
            return bd
        except Exception:
            raise ValueError("Birth date must be in 'YYYY/M/D' Jalali format and a valid date.")

    def _validate_national_id(self, national_id: str) -> str:
        if not re.fullmatch(r"\d{10}", national_id):
            raise ValueError("National ID must be exactly 10 digits.")
        return national_id

    def _validate_phone_number(self, phone_number: str) -> str:
        if not re.fullmatch(r"09\d{9}", phone_number):
            raise ValueError("Phone number must be 11 digits starting with '09'.")
        return phone_number

    def _validate_email(self, email: str) -> str:
        email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}"
        if not re.fullmatch(email_pattern, email):
            raise ValueError("Invalid email format.")
        return email.lower()

    def age(self) -> int:
        """Calculate age from birth_date using Jalali calendar."""
        today = jdatetime.date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def update_info(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'birth_date':
                self.birth_date = self._validate_birth_date(value)
            elif key == 'phone_number':
                self.phone_number = self._validate_phone_number(value)
            elif key == 'email':
                self.email = self._validate_email(value)
            elif key == 'name':
                self.name = self._validate_name(value)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "birth_date": self.birth_date.isoformat(),
            "age": self.age,
            "national_id": self.national_id,
            "phone_number": self.phone_number,
            "email": self.email,
            "stats": self.stats.to_dict(),
            "created_at": self.created_at
        }

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.national_id == other.national_id
        return False

    def __hash__(self):
        return hash(self.national_id)

    def __repr__(self):
        return f"Person(name='{self.name}', birth_date='{self.birth_date}', national_id='{self.national_id}')"

    def __str__(self):
        return f"{self.name} (ID: {self.national_id}, Age: {self.age})"


class Section:
    """Represents a company section/department."""
    
    def __init__(self, name: str, description: str, phone_number: str, manager: Optional[Person] = None):
        self.name = self._validate_name(name)
        self.description = description
        self.phone_number = self._validate_phone_number(phone_number)
        self.manager = manager
        self.employees: List[Person] = []
        self.created_at = datetime.now().isoformat()

    def _validate_name(self, name: str) -> str:
        """Validate section name."""
        if not name or len(name.strip()) < 2:
            raise ValueError("Section name must be at least 2 characters long.")
        return name.strip()

    def _validate_phone_number(self, phone_number: str) -> str:
        """Validate phone number format."""
        if not re.fullmatch(r"09\d{9}", phone_number):
            raise ValueError("Phone number must be 11 digits starting with '09'.")
        return phone_number

    def set_manager(self, manager: Person):
        """Set section manager."""
        self.manager = manager
        if manager not in self.employees:
            self.add_employee(manager)

    def add_employee(self, employee: Person):
        """Add employee to section."""
        if employee not in self.employees:
            self.employees.append(employee)
            employee.stats._update_employed(True)
        else:
            raise ValueError(f"Employee {employee.name} is already in this section.")

    def remove_employee(self, employee: Person):
        """Remove employee from section."""
        if employee in self.employees:
            self.employees.remove(employee)
            employee.stats._update_employed(False)
            if self.manager == employee:
                self.manager = None
        else:
            raise ValueError(f"Employee {employee.name} is not in this section.")

    def get_employee_stats(self) -> List[Dict[str, Any]]:
        """Get statistics for all employees."""
        return [employee.stats.to_dict() for employee in self.employees]

    def get_working_employees(self) -> List[Person]:
        """Get list of currently working employees."""
        return [emp for emp in self.employees if emp.stats.working]

    def get_employed_count(self) -> int:
        """Get total number of employees."""
        return len(self.employees)

    def get_working_count(self) -> int:
        """Get number of working employees."""
        return len(self.get_working_employees())

    def set_employee_working_status(self, employee: Person, working: bool):
        """Set working status for an employee."""
        if employee in self.employees:
            employee.stats._update_working(working)
        else:
            raise ValueError(f"Employee {employee.name} is not in this section.")

    def get_employees_by_age_range(self, min_age: int, max_age: int) -> List[Person]:
        """Get employees within specified age range."""
        return [emp for emp in self.employees if min_age <= emp.age <= max_age]

    def find_employee_by_name(self, name: str) -> Optional[Person]:
        """Find employee by name (case-insensitive)."""
        name_lower = name.lower()
        return next((emp for emp in self.employees if emp.name.lower() == name_lower), None)

    def find_employee_by_id(self, national_id: str) -> Optional[Person]:
        """Find employee by national ID."""
        return next((emp for emp in self.employees if emp.national_id == national_id), None)

    def get_employee_summary(self) -> Dict[str, Any]:
        """Get comprehensive summary of section employees."""
        return {
            "total_employees": self.get_employed_count(),
            "working_employees": self.get_working_count(),
            "average_age": sum(emp.age() for emp in self.employees) / len(self.employees) if self.employees else 0,
            "age_distribution": {
                "18-25": len([emp for emp in self.employees if 18 <= emp.age() <= 25]),
                "26-35": len([emp for emp in self.employees if 26 <= emp.age() <= 35]),
                "36-45": len([emp for emp in self.employees if 36 <= emp.age() <= 45]),
                "46+": len([emp for emp in self.employees if emp.age() > 45])
            },
            "manager": self.manager.name if self.manager else None
        }

    def to_dict(self) -> Dict[str, Any]:
        """Convert section to dictionary format."""
        return {
            "name": self.name,
            "description": self.description,
            "phone_number": self.phone_number,
            "manager": self.manager.to_dict() if self.manager else None,
            "employees": [emp.to_dict() for emp in self.employees],
            "created_at": self.created_at,
            "summary": self.get_employee_summary()
        }

    # Magic methods
    def __len__(self):
        return len(self.employees)

    def __contains__(self, employee: Person):
        return employee in self.employees

    def __iter__(self):
        return iter(self.employees)

    def __getitem__(self, index):
        return self.employees[index]

    def __bool__(self):
        return len(self.employees) > 0

    def __repr__(self):
        return f"Section(name='{self.name}', employees={len(self.employees)})"

    def __str__(self):
        manager_info = f", Manager: {self.manager.name}" if self.manager else ""
        return f"Section '{self.name}': {len(self.employees)} employees{manager_info}"

class Company:
    """Represents a company with multiple sections and employees."""
    
    def __init__(self, name: str, founding_year: int, initial_budget: float, email: str, phone_number: str):
        self.name = self._validate_name(name)
        self.founding_year = self._validate_founding_year(founding_year)
        self.initial_budget = self._validate_budget(initial_budget)
        self.email = self._validate_email(email)
        self.phone_number = self._validate_phone_number(phone_number)
        self.sections: Dict[str, Section] = {}
        self.created_at = datetime.now().isoformat()

    def _validate_name(self, name: str) -> str:
        """Validate company name."""
        if not name or len(name.strip()) < 2:
            raise ValueError("Company name must be at least 2 characters long.")
        return name.strip()

    def _validate_founding_year(self, year: int) -> int:
        """Validate founding year."""
        current_year = datetime.now().year
        if not isinstance(year, int) or not (1800 <= year <= current_year):
            raise ValueError(f"Founding year must be between 1800 and {current_year}.")
        return year

    def _validate_budget(self, budget: float) -> float:
        """Validate budget amount."""
        if not isinstance(budget, (int, float)) or budget < 0:
            raise ValueError("Budget must be a non-negative number.")
        return float(budget)

    def _validate_email(self, email: str) -> str:
        """Validate email format."""
        email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}"
        if not re.fullmatch(email_pattern, email):
            raise ValueError("Invalid email format.")
        return email.lower()

    def _validate_phone_number(self, phone_number: str) -> str:
        """Validate phone number format."""
        if not re.fullmatch(r"09\d{9}", phone_number):
            raise ValueError("Phone number must be 11 digits starting with '09'.")
        return phone_number

    def add_section(self, section: Section):
        """Add section to company."""
        if section.name not in self.sections:
            self.sections[section.name] = section
        else:
            raise ValueError(f"Section with name '{section.name}' already exists.")

    def remove_section(self, section_name: str):
        """Remove section from company by name."""
        if section_name in self.sections:
            del self.sections[section_name]
        else:
            raise ValueError(f"Section '{section_name}' not found in company.")

    def get_section(self, name: str) -> Optional[Section]:
        """Get section by name."""
        return self.sections.get(name)

    def find_section_by_name(self, name: str) -> Optional[Section]:
        """Find section by name (case-insensitive)."""
        name_lower = name.lower()
        for section_name, section in self.sections.items():
            if section_name.lower() == name_lower:
                return section
        return None

    def find_employee_by_name(self, name: str) -> Optional[Person]:
        """Find employee across all sections by name."""
        for section in self.sections.values():
            emp = section.find_employee_by_name(name)
            if emp:
                return emp
        return None

    def find_employee_by_id(self, national_id: str) -> Optional[Person]:
        """Find employee across all sections by national ID."""
        for section in self.sections.values():
            emp = section.find_employee_by_id(national_id)
            if emp:
                return emp
        return None

    def get_all_employees(self) -> List[Person]:
        """Get all employees across all sections."""
        all_employees = []
        for section in self.sections.values():
            all_employees.extend(section.employees)
        return all_employees

    def get_section_stats(self) -> List[Dict[str, Any]]:
        """Get statistics for all sections."""
        return [section.get_employee_summary() for section in self.sections.values()]

    def get_total_employees(self) -> int:
        """Get total number of employees across all sections."""
        return sum(len(section) for section in self.sections.values())

    def get_company_summary(self) -> Dict[str, Any]:
        """Get comprehensive company summary."""
        all_employees = self.get_all_employees()
        return {
            "company_info": {
                "name": self.name,
                "founding_year": self.founding_year,
                "age": datetime.now().year - self.founding_year,
                "initial_budget": self.initial_budget,
                "total_sections": len(self.sections),
                "total_employees": len(all_employees)
            },
            "employee_statistics": {
                "working_employees": len([emp for emp in all_employees if emp.stats.working]),
                "average_age": sum(emp.age() for emp in all_employees) / len(all_employees) if all_employees else 0,
                "age_distribution": {
                    "18-25": len([emp for emp in all_employees if 18 <= emp.age() <= 25]),
                    "26-35": len([emp for emp in all_employees if 26 <= emp.age() <= 35]),
                    "36-45": len([emp for emp in all_employees if 36 <= emp.age() <= 45]),
                    "46+": len([emp for emp in all_employees if emp.age() > 45])
                }
            },
            "sections": [section.get_employee_summary() for section in self.sections.values()]
        }

    def to_dict(self) -> Dict[str, Any]:
        """Convert company to dictionary format."""
        return {
            "company_info": {
                "name": self.name,
                "founding_year": self.founding_year,
                "initial_budget": self.initial_budget,
                "email": self.email,
                "phone_number": self.phone_number,
                "created_at": self.created_at
            },
            "sections": {name: section.to_dict() for name, section in self.sections.items()},
            "summary": self.get_company_summary()
        }

    def __len__(self):
        """Return total number of employees."""
        return self.get_total_employees()

    def __contains__(self, item):
        """Check if section or employee exists in company."""
        if isinstance(item, Section):
            return item in self.sections.values()
        elif isinstance(item, Person):
            return any(item in section for section in self.sections.values())
        elif isinstance(item, str):
            return item in self.sections
        return False

    def __getitem__(self, section_name: str) -> Section:
        """Get section by name using bracket notation."""
        if section_name in self.sections:
            return self.sections[section_name]
        raise KeyError(f"Section '{section_name}' not found.")

    def __repr__(self):
        return f"Company(name='{self.name}', sections={len(self.sections)}, employees={self.get_total_employees()})"

    def __str__(self):
        return f"Company '{self.name}' (Est. {self.founding_year}): {len(self.sections)} sections, {self.get_total_employees()} employees"


# Example usage and testing
if __name__ == "__main__":
    # Create company
    company = Company("TechCorp", 2020, 1000000.0, "info@techcorp.com", "09123456789")
    
    # Create sections
    it_section = Section("IT", "Information Technology Department", "09111111111")
    hr_section = Section("HR", "Human Resources Department", "09222222222")

    # Add sections to company
    company.add_section(it_section)
    company.add_section(hr_section)
    
    # Create employees
    john = Person("John Doe", "1375/5/10", "1234567890", "09333333333", "john@example.com")
    jane = Person("Jane Smith", "1372/2/20", "0987654321", "09444444444", "jane@example.com")
    
    # Add employees to sections (now using dictionary access)
    company["IT"].add_employee(john)
    company["HR"].add_employee(jane)
    
    # Set working status
    company["IT"].set_employee_working_status(john, True)
    
    # Print summary
    print(company)
    summary = company.get_company_summary()
    
    # Pretty print using pprint with enhanced formatting
    print("\n" + "="*80)
    print("📊 COMPANY SUMMARY REPORT".center(80))
    print("="*80)
    
    # Configure pprint for better readability
    pp = PrettyPrinter(
        width=100,           # Wider output for better formatting
        depth=6,             # Allow deeper nesting
        indent=2,            # Clean indentation
        compact=False,       # Don't compact sequences
        sort_dicts=True      # Sort dictionary keys for consistency
    )
    
    print(f"\n🏢 Company: {company.name}")
    print(f"📅 Founded: {company.founding_year} ({datetime.now().year - company.founding_year} years old)")
    print(f"👥 Total Employees: {company.get_total_employees()}")
    print(f"🏬 Total Sections: {len(company.sections)}")
    
    print("\n" + "-"*80)
    print("📈 DETAILED STATISTICS")
    print("-"*80)
    
    pp.pprint(summary)
    
    print("\n" + "="*80)
    print("End of Report".center(80))
    print("="*80)
