import controller
import os.path


def criarArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write('')

criarArquivos('categoria.txt', 'clientes.txt', 
              'estoque.txt', 'fornecedores.txt', 
              'funcionarios.txt', 'venda.txt')

if __name__ == '__main__':
    while True:
        local = int(input(
            'Digite 1 para acessar ( Categorias )\n'
            'Digite 2 para acessar ( Estoque )\n'
            'Digite 3 para acessar ( Fornecedor )\n'
            'Digite 4 para acessar ( Cliente )\n'
            'Digite 5 para acessar ( Funcionario )\n'
            'Digite 6 para acessar ( Vendas )\n'
            'Digite 7 para ver os produtos mais vendidos\n'
            'Digite 8 para sair\n'
        ))

        if local == 1:
            cat = controller.ControllerCategoria()
            while True:
                decidir = int(input(
                    'Digite 1 para cadastrar uma categoria\n'
                    'Digite 2 para remover uma categoria\n'
                    'Digite 3 para alterar uma categoria\n'
                    'Digite 4 para mostrar as categorias cadastradas\n'
                    'Digite 5 para sair\n'
                ))
                if decidir == 1:
                    categoria = input('Digite a categoria que deseja cadastrar:\n')
                    cat.cadastrarCategoria(categoria)
                elif decidir == 2:
                    categoria = input('Digite a categopria que deseja remover:\n')
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input('Digite a categoria que deseja alterar:\n')
                    novaCategoria = input('Digite a categporia para qual deseja alterar:\n')
                    cat.alteraCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else:
                    break
        
        elif local == 2:
            cat = controller.ControllerEstoque()
            while True:
                decidir = int(input(
                    'Digite 1 para cadastrar um produto\n'
                    'Digite 2 para remover um produto\n'
                    'Digite 3 para alterar um produto\n'
                    'Digite 4 para ver o estoque\n'
                    'Digite 5 para sair\n'
                ))
                if decidir == 1:
                    nome = input('Digite o nome do produto:\n')
                    preco = input('Digite o preço do produto:\n')
                    categoria = input('Digite a categoria do produto:\n')
                    quantidade = input('Digite a categoria do produto:\n')
                    cat.cadastrarProduto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    produto = input('Digite o produto que deseja remover:\n')
                    cat.removerProduto(produto)
                elif decidir == 3:
                    nomeAlterar = input('Digite o nome do produto que deseja alterar:\n')
                    nome = input('Digite o novo nome do produto:\n')
                    preco = input('Digite o novo preço do produto:\n')
                    categoria = input('Digite a nova categoria do produto:\n')
                    quantidade = input('Digite a nova quantidade do produto:\n')
                    cat.alterarProduto(nomeAlterar, nome, preco, categoria, quantidade)
                elif decidir == 4:
                    cat.mostrarEstoque()
                else:
                    break

        elif local == 3:
            cat = controller.ControllerFornecedor()
            while True:
                decidir = int(input(
                    'Digite 1 para cadastrar um fornecedor\n'
                    'Digite 2 para remover um fornecedor\n'
                    'Digite 3 para alterar um fornecedor\n'
                    'Digite 4 para mostrar um fornecedor\n'
                    'Digite 5 para sair\n'
                ))
                if decidir == 1:
                    nome = input('Digite o nome do fornecedor:\n')
                    cnpj = input('Digite o cnpj do fornecedor\n')
                    telefone = input('Digite o telefone do fornecedor\n')
                    cat.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                elif decidir == 2:
                    fornecedor = input('Digite o fornecedor que deseja remover\n')
                    cat.removerFornecedor(fornecedor)
                elif decidir == 3:
                    nomeAlterar = input('Digite o nome do fornecedor que deseja alterar\n')
                    novoNome = input('Digite o novo nome do fornecedor\n')
                    novoCnpj = input('Dgite o novo cnpj do fornecedor\n')
                    novoTelefone = input('Dgite o novo telefone do fornecedor\n')
                    novaCategoria = input('Dgite o novo categoria do fornecedor\n')
                    cat.alterarFornecedor(nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria)
                elif decidir == 4:
                    cat.mostrarFornecedores()
                else:
                    break
        
        elif local == 4:
            cat = controller.ControllerCliente()
            while True:
                decidir = int(input(
                    'Digite 1 para cadastrar um cliente\n'
                    'Digite 2  para remover um cliente\n'
                    'Digite 3 para alterar um cliente\n'
                    'Digite 4 para mostrar clientes\n'
                    'Digite 5 para sair\n'
                ))
                if decidir == 1:
                    nome = input('Digite o nome do cliente\n')
                    telefone = input('Digite o telefone do cliente\n')
                    cpf = input('Digite o cpf do cliente\n')
                    email = input('Digite o email do cliente\n')
                    endereco = input('Digite o endereço do cliente\n')
                    cat.cadastrarCliente(nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    cliente = input('Digite o cliente que deseja remover\n')
                    cat.removerClientes(cliente)
                elif decidir == 3:
                    nomeAlterar = input('Digite o nome do cliente que deseja alterar\n')
                    novoNome = input('Digite o novo nome do cliente\n')
                    novoTelefone = input('Digite o novo telefone do cliente\n')
                    novoCpf = input('Digite o novo cpf do cliente\n')
                    novoEmail = input('Digite o novo email do cliente\n')
                    novoEndereco = input('Digite o novo endereço do cliente\n')
                    cat.alterarCliente(nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 4:
                    cat.mostrarClientes()
                else:
                    break
        
        elif local == 5:
            cat = controller.ControllerFuncionario()
            while True:
                decidir = int(input(
                    'Digite 1 para cadastrar um funcionário\n'
                    'Digite 2 para remover um funcionário\n'
                    'Digite 3 para alterar um funcionário\n'
                    'Digite 4 para mostrar um funcionário\n'
                    'Digite 5 para sair\n'
                ))
                if decidir == 1:
                    clt = input('Digite a clt do funcionário\n')
                    nome = input('Digite o nome do funcionário\n')
                    telefone = input('Digite o telefone do funcionário\n')
                    cpf = input('Digite o cpf do funcionário\n')
                    email = input('Digite o email do funcionário\n')
                    endereco = input('Digite o endereço do funcionário\n')
                    cat.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    funcionario = input('Digite o funcionário que deseja remover\n')
                    cat.removerFuncionario(funcionario)
                elif decidir == 3:
                    nomeAlterar = input('digite o nome do funcionário que deseja alterar\n')
                    novoClt = input('Digite a nova clt do funcionário\n')
                    novoNome = input('Digite o novo nome do funcionário\n')
                    novoTelefone = input('Digite o novo telefone do funcionário\n')
                    novoCpf = input('Digite o novo cpf do funcionário\n')
                    novoEmail = input('Digite o novo email do funcionário\n')
                    novoEndereco = input('Digite o novo endereço do funcionário\n')
                    cat.alterarFuncionario(nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 4:
                    cat.mostrarFuncionarios()
                else:
                    break

        elif local == 6:
            cat = controller.ControllerVenda()
            while True:
                decidir = int(input(
                    'Digite 1 para realizar uma venda\n'
                    'Digite 2 para ver as vendas\n'
                    'Digite 3 para sair\n'
                ))
                if decidir == 1:
                    nome = input('Digite o nome do produto\n')
                    vendedor = input('Digite o nome do vendedor\n')
                    comprador = input('Digite o nome do comprador\n')
                    quantidade = input('Digite a quantidade\n')
                    cat.cadastrarVenda(nome, vendedor, comprador, quantidade)
                elif decidir == 2:
                    dataInicio = input('Digite a data de inicio no formato dia/mês/ano\n')
                    dataTermino = input('Digite a data de termino no formato dia/mês/ano\n')
                    cat.mostrarVenda(dataInicio, dataTermino)
                elif decidir == 3:
                    break
        
        elif local == 7:
            cat = controller.ControllerVenda()
            cat.relatorioProdutos()
        else:
            break
