# Generated by Django 3.2.6 on 2021-10-06 21:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('extras', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('lang', models.CharField(default='0', max_length=255)),
                ('lat', models.CharField(default='0', max_length=255)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.cart')),
                ('ordered_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.instructor')),
                ('payment_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='extras.paymenttype')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('cart_item_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart_item_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item_owner', to='users.instructor')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_items',
            field=models.ManyToManyField(blank=True, to='orders.CartItem'),
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_owner', to='users.instructor'),
        ),
    ]
