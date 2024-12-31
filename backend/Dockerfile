# backend/Dockerfile
FROM python:3.12.5

WORKDIR /workspace
RUN pip install fastapi uvicorn[standard] --no-cashe-dir
CMD ["uvicorn", "main:app", "--reload"]