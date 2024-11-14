
## Rapport TP

### 1
sudo apt update
sudo apt install gitlab-runner
pip install --upgrade pip
pip install hatch



### 2

Créer le projet :
```bash
    hatch new my-arithmetic-$(whoami)
    cd my-arithmetic-$(whoami)
```

Ajout du code :
```Python
    # src/makr/__init__.py
    def pgcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

        
    # tests/test_pgcd.py
    import pytest
    from my_arithmetic_svalerio import pgcd

def test_pgcd():
    assert pgcd(56, 98) == 14
    assert pgcd(101, 10) == 1
    assert pgcd(30, 45) == 15
    assert pgcd(13, 13) == 13
    assert pgcd(0, 5) == 5
```


Lancer les tests en Local :
```bash
    hatch shell
    hatch test
```

Résultat : 
```bash
    ================================================================== test session starts ===================================================================
    platform darwin -- Python 3.13.0, pytest-8.3.3, pluggy-1.5.0
    rootdir: /Users/svalerio//my-arithmetic-svalerio
    configfile: pyproject.toml
    plugins: rerunfailures-14.0, mock-3.14.0, xdist-3.6.1
    collected 1 item                                                                                                                                         

    tests/test_gcd.py .                                                                                                                                [100%]

    =================================================================== 1 passed in 0.02s ====================================================================
```


### 3

Création du repo GitLab + Init runner (tags = coverage) du projet.

Créer un runner sur GitLab Setting > CI/CD :
```bash
    [tags] -> docker, test-job
    [description] -> docker-runner
```

Terminal association runner  :
```bash
    sudo gitlab-runner register
    sudo gitlab-runner run

```

Configurer le .gitlab-ci pour créer la pipeline test ainsi que le bagde:
```yml
    stages:
  - test

test-job:
  stage: test
  script:
    - export PYTHONPATH=$PYTHONPATH:$(pwd)/src
    - apk add gcc python3-dev musl-dev linux-headers
    - pip install --upgrade pip
    - pip install hatch
    - pip install pytest pytest-cov
    - hatch test
    - pytest --cov=src.my_arithmetic_svalerio.__init__ --cov-report=xml --cov-report=term-missing 
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml 
  coverage: '/TOTAL.*? (\d+\%)$/'   
  tags: 
    - docker


### 5

Generer un token GitHub dans Settings > Developer Settings > Personal access tokens (classic)

Puis on remplit le formulaire GitLab > Repository Settings > Mirroring repositories
