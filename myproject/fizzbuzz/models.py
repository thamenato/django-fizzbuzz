from django.db import models


class Fizzbuzz(models.Model):
    fizzbuzz_id = models.AutoField(primary_key=True)
    useragent = models.TextField(blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=False)

    class Meta:
        ordering = ["fizzbuzz_id"]

    def __str__(self) -> str:
        return f"{self.fizzbuzz_id} | {self.creation_date} | {self.useragent} | {self.message}"
