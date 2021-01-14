# code_profiler
Version: 2.0

Автор: Полтораднев Кирилл
Дата: 14.01.2021

## Описание
Утилита краулер позволяет профилировать код методом семплирования.

## Состав
* Файл запуска утилиты: `profiler.py`
* Модули: `/modules`
* Тесты: `/tests`

### Управление
`profiler.py [-h] [-w WORKDIR] [-s SORTBY] [-o OUTPUT] [-i INTERVAL] program argv [argv ...]`

Для работы утилита использует параметры:

*  `program_path` путь до профилируемого файла
* `-h`, `--help` отобразить сообщение help
* `-w WORKDIR` указать рабочую директорию
* `-s SORTBY` указать параметр сортировки данныз (по умолчанию: time)
* `-o OUTPUT` указать файл сохранения статистики (файл должен быть без формата)
* `-i INTERVAL` указать интервал копии стека (по умолчанию: 10 мс)
* `program` имя файла профилирования
* `-argv [argv ...]` указать аругументы [agrv..] запуска для указанного файла program (по умолчанию: None)

### Пример использования фильтров
`python3 profiler.py -w ./tests/ -o prog_prof hello.py`

В данном примере происходит профилирование `hello.py` из папки `../code_profiler/tests/`. Результат будет сохранен в файл `../code_profiler/tests/prog_prof.csv`

`python3 profiler.py -w .\tests calculater.py  1 2 3 4`

В данном примере происходит профилирование `calculater.py`, запущенного с аргументами `1, 2, 3, 4`, из папки `../code_profiler/tests/`

## Подробности реализации
Модули, отвечающие за логику профайлера расположены в пакете modules. 
* `modules.Profiler`- класс, реализующий сбор данных стека вызов во время исполнения программы
* `modules.ProfilerCore` - класс, реализующий логику работы профайлера
* `modules.Statistics` - типы данных для подсчета статистики

