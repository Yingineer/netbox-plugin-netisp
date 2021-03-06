import django_tables2 as tables

from .models import Customer, Address
from utilities.tables import BaseTable, ButtonsColumn, ChoiceFieldColumn, TagColumn, ToggleColumn


class CustomerTable(BaseTable):
    pk = ToggleColumn()

    first_name = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = Customer
        fields = ( 'pk', 'first_name', 'middle_name', 'last_name', 'slug')


class AddressTable(BaseTable):
    pk = ToggleColumn()


    street_number = tables.LinkColumn()



    class Meta(BaseTable.Meta):
        model = Address
        fields = ( 'pk', 'street_number', 'street_name', 'street_suffix')