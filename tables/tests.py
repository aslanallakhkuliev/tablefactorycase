import pytest
from django.db import IntegrityError
from django.test import TransactionTestCase
from django.core.exceptions import ValidationError

from tables.models import Table, Leg, Foot


class TablesTest(TransactionTestCase):
    def test_create(self):
        Table(name="Table One").save()

        assert Table.objects.count() == 1
        assert Table.objects.get(pk=1).name == "Table One"

        with self.assertRaises(IntegrityError):
            Table(name="Table One").save()
        assert Table.objects.count() == 1

    def test_list(self):
        Table(name="Table One").save()
        Table(name="Table Two").save()
        Table(name="Table Three").save()

        assert Table.objects.count() == 3

    def test_detail(self):
        Table(pk=1, name="Table One").save()
        Table(pk=2, name="Table Two").save()
        Table(pk=3, name="Table Three").save()

        assert Table.objects.get(pk=2).name == "Table Two"

    def test_update(self):
        t1 = Table(pk=1, name="Table One")
        t1.save()
        t2 = Table(pk=2, name="Table Two")
        t2.save()
        t3 = Table(pk=3, name="Table Three")
        t3.save()

        with self.assertRaises(IntegrityError):
            t2.name = "Table One"
            t2.save()
        assert Table.objects.get(pk=2).name == "Table Two"

    def test_delete(self):
        Table(pk=1, name="Table One").save()
        Table(pk=2, name="Table Two").save()
        t3 = Table(pk=3, name="Table Three")
        t3.save()

        Table.objects.get(pk=3).delete()
        assert Table.objects.count() == 2


class LegsTest(TransactionTestCase):
    def test_create(self):
        t1 = Table(name="Table One")
        t1.save()
        t2 = Table(name="Table Two Unsaved")
        l1 = Leg(pk=1, table_id=t1)
        l1.save()

        assert Leg.objects.count() == 1
        assert Leg.objects.get(pk=1).table_id == t1

    def test_list(self):
        t1 = Table(name="Table One")
        t1.save()
        t2 = Table(name="Table Two")
        t2.save()
        Leg(table_id=t1).save()
        Leg(table_id=t2).save()

        assert Leg.objects.count() == 2

    def test_detail(self):
        t1 = Table(name="Table One")
        t1.save()
        t2 = Table(name="Table Two")
        t2.save()
        Leg(pk=1, table_id=t1).save()
        Leg(pk=2, table_id=t2).save()

        assert Leg.objects.get(pk=1).table_id == t1

    def test_update(self):
        t1 = Table(name="Table One")
        t1.save()
        t2 = Table(name="Table Two")
        t2.save()
        t3 = Table(name="Table Three Unsaved")
        l1 = Leg(pk=1, table_id=t1)
        l1.save()
        l1.table_id = t2
        l1.save()

        assert Leg.objects.get(pk=1).table_id == t2

        try:
            l1.table_id = t3
            l1.save()
        except ValueError:
            pass
        else:
            raise AssertionError("ValueError was not raised")

    def test_delete(self):
        t1 = Table(name="Table One")
        t1.save()
        l1 = Leg(pk=1, table_id=t1)
        l1.save()

        assert Leg.objects.count() == 1

        Leg.objects.get(pk=1).delete()
        assert Leg.objects.count() == 0


class FeetTest(TransactionTestCase):
    def test_all_methods(self):
        # Creating and listing objects.
        #
        t1 = Table(pk=1, name="Table One")
        t1.save()
        t2 = Table(pk=2, name="Table Two")
        t2.save()
        #
        l1 = Leg(table_id=t1)
        l1.save()
        l2 = Leg(table_id=t2)
        l2.save()
        #
        f1 = Foot(pk=1, radius=1)
        f1.save()
        f1.legs.set([l1, l2])
        f1.save()
        f2 = Foot(pk=2, length=15, width=2.7)
        f2.save()
        f2.legs.set([l1, l2])
        f2.save()
        #
        assert Foot.objects.count() == 2
        assert Foot.objects.get(pk=1).radius == 1
        assert Foot.objects.get(pk=2).length == 15

        # Checking the validation
        #
        with pytest.raises(ValidationError) as excinfo:
            f3 = Foot(pk=3, radius=1, length=3.5)
            f3.save()
        assert "ValidationError" in str(excinfo)
        #
        with pytest.raises(ValidationError) as excinfo:
            f3 = Foot(pk=3, length=17)
            f3.save()
        assert "ValidationError" in str(excinfo)
        #
        with pytest.raises(ValidationError) as excinfo:
            f3 = Foot(pk=3, width=3.5)
            f3.save()
        assert "ValidationError" in str(excinfo)

        # Updating the object
        #
        f1.radius = 1.75
        f1.save()
        #
        assert Foot.objects.get(pk=1).radius == 1.75

        # Deleting the object
        #
        assert Foot.objects.count() == 2
        #
        Foot.objects.get(pk=2).delete()
        assert Foot.objects.count() == 1
