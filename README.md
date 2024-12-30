

# Run weaviate vector db

`docker-compose up`

Above command should be sufficient enough, but pull this image if needed. `docker pull cr.weaviate.io/semitechnologies/weaviate:1.26.5`


# Poetry dependency management
`brew install poetry`

`poetry shell` - run virtual environment


# Jupyter notebook
`pip install notebook ipykernel`

Use the virtual environment created using poetry shell as kernel for the jupyter notebook

```
python -m ipykernel install --user --name=oncall-agent-py3.13 --display-name "oncall_agent_test"
```

