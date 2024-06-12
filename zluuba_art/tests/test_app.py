def test_home(client):
    response = client.get('/')

    assert response.status_code == 200
    assert b'You can call me Lua.' in response.data


def test_cv_page(client):
    response = client.get('/cv')

    assert response.status_code == 200
    assert b'CV' in response.data
    assert b'zluyba.nikitina@gmail.com' in response.data


def test_projects_page(client):
    response = client.get('/projects')

    assert response.status_code == 200
    assert b'Projects' in response.data
    assert b'Games Of Terminal' in response.data
    assert b'Task Manager' in response.data


def test_links_page(client):
    response = client.get('/links')

    assert response.status_code == 200
    assert b'Links' in response.data
    assert b'GitHub' in response.data
    assert b'Telegram' in response.data


def test_page_analyzer_projects_page(client):
    response = client.get('/projects/page-analyzer')

    assert response.status_code == 200
    assert b'Page Analyzer' in response.data
    assert b'Screenshots' in response.data


def test_robots_page(client):
    response = client.get('/robots.txt')

    assert response.status_code == 200
    assert b'robots.txt file for www.zluuba.art website' in response.data
    assert b'User-agent' in response.data


def test_404_error_page(client):
    response = client.get('/non-existent-path')

    assert response.status_code == 404
    assert b'Page Not Found' in response.data
    assert b'Go Home' in response.data
