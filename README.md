REST-like web service that provides a single endpoint `gene_suggest`.

The endpoint accepts the following arguments
•	table - name of the table for search
•	query - the partial query typed by the user, e.g. `brc` (as in the example above)
•	species - the name of the target species, e.g. `homo_sapiens`
•	limit - the maximum number of suggestions to return, e.g. `10`

If there is no any arguments enpoint use this default arguments:
table=gene_autocomplete
species=homo_sapiens
label=BRC%
limit=2

The endpoint needs for correct work following pakages: 
Click==7.0
Flask==1.1.1
Flask-Jsonpify==1.5.0
Flask-RESTful==0.3.7
Jinja2==2.10.1
MarkupSafe==1.1.1
PyMySQL==0.9.3
SQLAlchemy==1.3.8
Werkzeug==0.16.0
aniso8601==8.0.0
itsdangerous==1.1.0
pip==19.0.3
pytz==2019.2
setuptools==40.8.0
six==1.12.0

Please use this or next version of packages. It also provides venv package for fast run.

Examples:
(a) http://127.0.0.1:5000/gene_suggest - default search
(b) http://127.0.0.1:5000/gene_suggest?table=gene_autocomplete&species=homo_sapiens&label=BRC%%&limit=2 - default parametrs
(c) http://127.0.0.1:5000/gene_suggest?table=gene_autocomplete&species=homo_sapiens&label=BRCA1&limit=2
(d) http://127.0.0.1:5000/gene_suggest?table=gene_autocomplete&species=homo_sapiens&label=BRCC3P1&limit=2
Note: You should use %% instead % for correct processing SQL-query. You IP may be 0.0.0.0 instead of 127.0.0.1 it depends on your OS.

Output: json-file with gene data

Output for examples:
(a): {"search": [{"species": "homo_sapiens", "stable_id": "ENSG00000012048", "display_label": "BRCA1", "location": "17:43044295-43170245", "db": "core"}, {"species": "homo_sapiens", "stable_id": "ENSG00000139618", "display_label": "BRCA2", "location": "13:32315474-32400266", "db": "core"}]}
(c): {"search": [{"species": "homo_sapiens", "stable_id": "ENSG00000012048", "display_label": "BRCA1", "location": "17:43044295-43170245", "db": "core"}, {"species": "homo_sapiens", "stable_id": "ENSG00000139618", "display_label": "BRCA2", "location": "13:32315474-32400266", "db": "core"}]}
(d): {"search": [{"species": "homo_sapiens", "stable_id": "ENSG00000012048", "display_label": "BRCA1", "location": "17:43044295-43170245", "db": "core"}]}
(e): {"search": [{"species": "homo_sapiens", "stable_id": "ENSG00000251667", "display_label": "BRCC3P1", "location": "5:176308063-176309013", "db": "core"}]}