from src.database.data_generator import DataGenerator

def test_DataGenerator_samples_returns_list():
    fake = DataGenerator()
    test_dict = {
        "instance1" : fake.sample_associado(1),
        "instance2" : fake.sample_cartao(1),
        "instance3" : fake.sample_conta(1),
        "instance4" : fake.sample_movimento(1)
    }

    for instance, result in test_dict.items():
        assert isinstance(result, list)
