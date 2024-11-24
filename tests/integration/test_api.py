from fastapi.testclient import TestClient

from sequences.main import app


client = TestClient(app)


def test_server_online():
    response = client.get("/")
    assert response.status_code == 200


def test_nucleotide_base():
    response = client.get("/nucleotides/bases")
    assert response.status_code == 200
    assert response.json()["bases"] == "ATCG"


def test_iupac_nucleotides():
    response = client.get("/iupac/nucleotides/R")
    assert response.status_code == 200
    assert response.json()["iupac_code"] == "R"
    assert response.json()["iupac_nucleotides"] == ["A", "G"]


def test_iupac_nucleotides_wrong_input():
    response = client.get("/iupac/nucleotides/P")
    assert response.status_code == 404


def test_profiel_past_in_spoor():
    cases = [
        ("ACTG", "ACTG", True),
        ("CCATGG", "YBATVN", True),
        ("TGATAC", "YBATVN", True),
        ("AAAAAA", "YBATVN", False),
        ("AAA", "YBATVN", False),
    ]
    for i in range(len(cases)):
        response = client.get(f"/app/past_in/{cases[i][0]}/{cases[i][1]}")
        assert response.json()["profiel_past_in_spoor"] == cases[i][2]


def test_profiel_past_in_spoor_wrong_input():
    response = client.get(f"/app/past_in/A/3")
    assert response.status_code == 404