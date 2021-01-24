# code_profiler
Version: 4.0

Автор: Полтораднев Кирилл
Дата: 24.01.2021

## Описание
Утилита позволяет профилировать код методом семплирования. Результат семплирования можно сохранить в отдельный .csv файл с дальнейшим подсчетом статискики

## Состав
* Файл утилиты профилирования: `profiler.py`
* Файл утилиты подсчета статистики на основе собранных данных: `calc_metrics.py`
* Модули: `/modules`
* Тесты: `/tests`

## Управление утилитой сбора статистики
`profiler.py  [-h] [-w WORKDIR] [-s SORTBY] [-o .csv] [-i INTERVAL] program [argv [argv ...]]`

Для работы утилита использует параметры:

* `-h`, `--help` отобразить сообщение help
* `-w WORKDIR` указать рабочую директорию
* `-s SORTBY` указать параметр сортировки данных (по умолчанию: time)
* `-o .csv` указать файл сохранения статистики (файл указывать без расширения)
* `-i INTERVAL` указать интервал копии стека (по умолчанию: 10 мс)
* `program` имя файла профилирования
* `[argv [argv ...]` указать аругументы ARGV запуска для указанного файла program (по умолчанию: None)

## Упарвление утилитой подсчета статистики
`calc_metrics.py [-h] [-s SORTBY] file`

Для работы утилита использует параметры:

* `-h`, `--help` отобразить сообщение help
* `-s SORTBY` указать параметр сортировки данных (по умолчанию: time)


### Пример использования фильтров
`python3 profiler.py -w ./tests/ -o prog_prof hello.py`

В данном примере происходит профилирование `hello.py` из папки `../code_profiler/tests/`. Результат будет сохранен в файл `../code_profiler/tests/prog_prof.csv`

`python3 profiler.py -w ./tests calculater.py 1 2 3 4`

В данном примере происходит профилирование `calculater.py`, запущенного с аргументами `1, 2, 3, 4`, из папки `../code_profiler/tests/`


## Формат вывода
`  Ordered by: time
  ncalls  tottime  percall  cumtime  percall  maxtime  mintime  medtime filename:(function) 
       2      6.0      3.0    18.01     9.01    5.982    5.982    5.982 calculater.py:(main)
       1        0      0.0    18.01    18.01        0        0        0 calculater.py:(<module>)
       1     0.01     0.01     3.02     3.02        0        0        0 calculater.py:(add_array)
       3     3.01      1.0     3.01      1.0    1.005    1.004    1.004 calculater.py:(add)
       1     0.01     0.01     3.01     3.01        0        0        0 calculater.py:(subtract_array)
       1     0.01     0.01     3.01     3.01        0        0        0 calculater.py:(divide_array)
       3      3.0      1.0      3.0      1.0    1.003    0.998    1.002 calculater.py:(subtract)
       3      3.0      1.0      3.0      1.0    1.001      1.0      1.0 calculater.py:(multiply)
       1      0.0      0.0      3.0      3.0        0        0        0 calculater.py:(multiply_array)
       3      3.0      1.0      3.0      1.0    1.004      1.0    1.001 calculater.py:(divide)
`
* `ncalls` - кол-во вызово
* `tottime` - время работы
* `cumtime` - комулятивное время работы
* `percall` - среднее время работы
* `percall` - отношение комулятивного времени на время работы
* `maxtime` - максимально время работы
* `mintime` - минимальное время работы
* `medtime` - медианное время работы

## Подробности реализации
Модули, отвечающие за логику профайлера расположены в пакете modules. 
* `modules.Profiler`- класс, реализующий сбор данных стека вызов во время исполнения программы
* `modules.ProfilerCore` - класс, реализующий логику работы профайлера
* `modules.Statistics` - типы данных для подсчета статистики
* `modules.OutputFormatter` - класс, обрабатывающий вывод статистик в консоль
* `modules.StatisticCalculator` - класс, подсчета статистик на основе raw-data

