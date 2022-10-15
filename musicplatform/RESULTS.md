### list all artists

```python
    from artists import Artist
    Artist.objects.all()
```
### result

```commandline
    <QuerySet [<Artist: ahmed gamal>, <Artist: amr>, <Artist: name1>, <Artist: name2>, <Artist: shereen>]>
```

---

### list down all artists sorted by name

```python
    Artist.objects.order_by('stage_name')
```

### result

```commandline
    <QuerySet [<Artist: ahmed gamal>, <Artist: amr>, <Artist: name1>, <Artist: name2>, <Artist: shereen>]>
```

---

### list down all artists whose name starts with 'a'

```python
    Artist.objects.filter(stage_name__startswith='a')
```

### result

```commandline
    <QuerySet [<Artist: ahmed gamal>, <Artist: amr>]>
```

---

### create some albums and assign them to any artists

#### method 1

```python
    from django.utils import timezone
    x = Artist.objects.get(stage_name='ahmed gamal')
    t = timezone.now()
    x.album_set.create(name='created through shell', cost=90, release_date=t)
```

#### result 1

```commandline
    <Album: created through shell>
```

#### method 2

```python
    from albums.models import Album
    tmp = Album(artist=x, name='created through shell again', cost=290, release_date=timezone.now())
    tmp.save()
```

#### result 2

```commandline
    <Album: created through shell again>
```

---

### get the latest released album

```python
    Album.objects.order_by('-release_date')[0]
```

### result

```commandline
    <Album: created through shell again>
```

---

### get all albums release before today 
```python
    x = Album.objects.filter(release_date__day__lt=timezone.datetime.now().day)
```

### result

```commandline
    <QuerySet [<Album: New Album>, <Album: New Album 2>, <Album: anything>, <Album: created through shell>, <Album: created through shell again>]>    
```

---

### get all albums released today or before today but not after today

```python
    Album.objects.all().filter(release_date__day__lte=timezone.now().day)
```

### result

```commandline
    <QuerySet [<Album: New Album>, <Album: New Album 2>, <Album: anything>, <Album: created through shell>, <Album: created through shell again>, <Album: released today>]>
```


---

### count the total number of albums

```python
    Album.objects.count()
```

### result

```commandline
    5
```


---

### In 2 different ways for each artist, list down all of his/her albums

#### method 1

```python
    x = list(Artist.objects.all())
    for a in x:
        a.album_set.values()
```

### result 1

```commandline
    <QuerySet [{'id': 1, 'artist_id': 4, 'name': 'New Album', 'creation_date': datetime.datetime(2022, 10, 14, 20, 55, 41, tzinfo=datetime.timezone.utc), 'release_date': datetime.datetime(2022, 10, 14, 20, 55, 44, tzinfo=datetime.timezone.utc), 'cost': 90.9}, {'id': 2, 'artist_id': 4, 'name': 'New Album 2', 'creation_date': datetime.datetime(2022, 10, 14, 20, 56, 10, tzinfo=datetime.timezone.utc), 'release_date': datetime.datetime(2022, 10, 14, 20, 56, 13, tzinfo=datetime.timezone.utc), 'cost': 30.0}, {'id': 4, 'artist_id': 4, 'name': 'created through shell', 'creation_date': datetime.datetime(2022, 10, 14, 21, 9, 42, 276176, tzinfo=datetime.timezone.utc), 'release_date': datetime.datetime(2022, 10, 14, 21, 8, 51, 311115, tzinfo=datetime.timezone.utc), 'cost': 90.0}, {'id': 5, 'artist_id': 4, 'name': 'created through shell again', 'creation_date': datetime.datetime(2022, 10, 14, 21, 14, 1, 807808, tzinfo=datetime.timezone.utc), 'release_date': datetime.datetime(2022, 10, 14, 21, 14, 1, 807660, tzinfo=datetime.timezone.utc), 'cost': 290.0}]>
    <QuerySet []>
    <QuerySet []>
    <QuerySet []>
    <QuerySet [{'id': 3, 'artist_id': 3, 'name': 'anything', 'creation_date': datetime.datetime(2022, 10, 14, 20, 56, 39, tzinfo=datetime.timezone.utc), 'release_date': datetime.datetime(2022, 10, 14, 20, 56, 41, tzinfo=datetime.timezone.utc), 'cost': 10000.0}]>
```

### method 2

```python
    first = Artist.objects.get(stage_name='ahmed gamal')
    first.album_set.values()
    second = Artist.objects.get(stage_name='shereen')
    second.album_set.values()
```

### result 2

```commandline
    <QuerySet [{'id': 1, 'artist_id': 4, 'name': 'New Album', 'creation_date': datetime.datetime(2022, 10, 14, 20, 55, 41, tzinfo=datetime.timezone.utc), 'release_date': datetime.datetime(2022, 10, 14, 20, 55, 44, tzinfo=datetime.timezone.utc), 'cost': 90.9}, {'id': 2, 'artist_id': 4, 'name': 'New Album 2', 'creation_date': datetime.datetime(2022, 10, 14, 20, 56, 10, tzinfo=datetime.timezone.utc), 'release_date': datetime.datetime(2022, 10, 14, 20, 56, 13, tzinfo=datetime.timezone.utc), 'cost': 30.0}, {'id': 4, 'artist_id': 4, 'name': 'created through shell', 'creation_date': datetime.datetime(2022, 10, 14, 21, 9, 42, 276176, tzinfo=datetime.timezone.utc), 'release_date': datetime.datetime(2022, 10, 14, 21, 8, 51, 311115, tzinfo=datetime.timezone.utc), 'cost': 90.0}, {'id': 5, 'artist_id': 4, 'name': 'created through shell again', 'creation_date': datetime.datetime(2022, 10, 14, 21, 14, 1, 807808, tzinfo=datetime.timezone.utc), 'release_date': datetime.datetime(2022, 10, 14, 21, 14, 1, 807660, tzinfo=datetime.timezone.utc), 'cost': 290.0}]>
    <QuerySet [{'id': 3, 'artist_id': 3, 'name': 'anything', 'creation_date': datetime.datetime(2022, 10, 14, 20, 56, 39, tzinfo=datetime.timezone.utc), 'release_date': datetime.datetime(2022, 10, 14, 20, 56, 41, tzinfo=datetime.timezone.utc), 'cost': 10000.0}]>
```
---

### list down all albums ordered by cost then by name (cost has the higher priority)

```python
    Album.objects.order_by('cost', 'name')
```

### result

```commandline
    <QuerySet [<Album: New Album 2>, <Album: created through shell>, <Album: New Album>, <Album: released today>, <Album: created through shell again>, <Album: anything>]>
```
