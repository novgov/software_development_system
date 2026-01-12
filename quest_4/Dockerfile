FROM jupyter/base-notebook:latest

# Устанавливаем системные зависимости для сборки C/C++ пакетов
USER root
RUN apt-get update && \
    apt-get install -y build-essential python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Возвращаемся к пользователю jovyan
USER jovyan

# Устанавливаем Python-пакеты
RUN pip install --no-cache-dir seaborn matplotlib pandas numpy scikit-learn ydata-profiling
