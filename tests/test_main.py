import task_manager_cli.main as main


def test_add_task(monkeypatch):
    main.tasks.clear()
    main.next_task_id = 1

    inputs = iter(["Learn Python", "Practice Python functions"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.add_task()

    assert len(main.tasks) == 1
    assert main.tasks[0]["id"] == 1
    assert main.tasks[0]["title"] == "Learn Python"
    assert main.tasks[0]["description"] == "Practice Python functions"
    assert main.tasks[0]["status"] == "pending"


def test_mark_task_completed(monkeypatch):
    main.tasks.clear()

    main.tasks.append(
        {
            "id": 1,
            "title": "Learn Python",
            "description": "Practice Python",
            "status": "pending",
        }
    )

    monkeypatch.setattr("builtins.input", lambda _: "1")

    main.mark_task_completed()

    assert main.tasks[0]["status"] == "completed"


def test_delete_task(monkeypatch):
    main.tasks.clear()

    main.tasks.append(
        {
            "id": 1,
            "title": "Learn Python",
            "description": "Practice Python",
            "status": "pending",
        }
    )

    monkeypatch.setattr("builtins.input", lambda _: "1")

    main.delete_task()

    assert len(main.tasks) == 0


def test_mark_task_completed_invalid_input(monkeypatch, capsys):
    main.tasks.clear()

    main.tasks.append(
        {
            "id": 1,
            "title": "Learn Python",
            "description": "Practice Python",
            "status": "pending",
        }
    )

    monkeypatch.setattr("builtins.input", lambda _: "abc")

    main.mark_task_completed()

    captured = capsys.readouterr()

    assert "Invalid input" in captured.out
    assert main.tasks[0]["status"] == "pending"


def test_view_tasks_when_empty(capsys):
    main.tasks.clear()

    main.view_tasks()

    captured = capsys.readouterr()

    assert "No tasks available" in captured.out


def test_add_task_with_blank_title(monkeypatch, capsys):
    main.tasks.clear()
    main.next_task_id = 1

    inputs = iter(["   ", ""])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.add_task()

    captured = capsys.readouterr()

    assert len(main.tasks) == 0
    assert "title" in captured.out.lower()


def test_delete_task_invalid_input(monkeypatch, capsys):
    main.tasks.clear()

    main.tasks.append(
        {
            "id": 1,
            "title": "Learn Python",
            "description": "Practice Python",
            "status": "pending",
        }
    )

    monkeypatch.setattr("builtins.input", lambda _: "abc")

    main.delete_task()

    captured = capsys.readouterr()

    assert len(main.tasks) == 1
    assert "Invalid input" in captured.out


def test_delete_non_existing_task(monkeypatch, capsys):
    main.tasks.clear()

    main.tasks.append(
        {
            "id": 1,
            "title": "Learn Python",
            "description": "Practice Python",
            "status": "pending",
        }
    )

    monkeypatch.setattr("builtins.input", lambda _: "99")

    main.delete_task()

    captured = capsys.readouterr()

    assert len(main.tasks) == 1
    assert "not found" in captured.out.lower()


def test_mark_already_completed_task(monkeypatch, capsys):
    main.tasks.clear()

    main.tasks.append(
        {
            "id": 1,
            "title": "Learn Python",
            "description": "Practice Python",
            "status": "completed",
        }
    )

    monkeypatch.setattr("builtins.input", lambda _: "1")

    main.mark_task_completed()

    captured = capsys.readouterr()

    assert main.tasks[0]["status"] == "completed"
    assert "already" in captured.out.lower()


def test_add_multiple_tasks(monkeypatch):
    main.tasks.clear()
    main.next_task_id = 1

    inputs = iter(
        ["Learn Python", "Practice functions", "Learn AWS", "Practice Lambda"]
    )

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.add_task()
    main.add_task()

    assert len(main.tasks) == 2
    assert main.tasks[0]["id"] == 1
    assert main.tasks[1]["id"] == 2
    assert main.tasks[0]["title"] == "Learn Python"
    assert main.tasks[1]["title"] == "Learn AWS"


def test_save_tasks(tmp_path, monkeypatch):
    test_file = tmp_path / "test_tasks.json"

    monkeypatch.setattr(main, "DATA_FILE", test_file)

    main.tasks.clear()

    main.tasks.append(
        {
            "id": 1,
            "title": "Learn Python",
            "description": "Practice Python",
            "status": "pending",
        }
    )

    main.save_tasks()

    assert test_file.exists()


def test_load_tasks(tmp_path, monkeypatch):
    test_file = tmp_path / "test_tasks.json"

    test_file.write_text(
        '[{"id": 1, "title": "Learn Python", '
        '"description": "Practice Python", '
        '"status": "pending"}]',
        encoding="utf-8",
    )

    monkeypatch.setattr(main, "DATA_FILE", test_file)

    loaded_tasks = main.load_tasks()

    assert len(loaded_tasks) == 1
    assert loaded_tasks[0]["id"] == 1
    assert loaded_tasks[0]["title"] == "Learn Python"
    assert loaded_tasks[0]["status"] == "pending"


def test_load_invalid_json(tmp_path, monkeypatch, capsys):
    test_file = tmp_path / "test_tasks.json"

    test_file.write_text("This is not valid JSON", encoding="utf-8")

    monkeypatch.setattr(main, "DATA_FILE", test_file)

    loaded_tasks = main.load_tasks()

    captured = capsys.readouterr()

    assert loaded_tasks == []
    assert "invalid JSON" in captured.out


def test_load_tasks_when_file_does_not_exist(tmp_path, monkeypatch):
    test_file = tmp_path / "missing_tasks.json"

    monkeypatch.setattr(main, "DATA_FILE", test_file)

    loaded_tasks = main.load_tasks()

    assert loaded_tasks == []
    assert not test_file.exists()
