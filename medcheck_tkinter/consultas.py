from persistencia import carregar_consultas, salvar_consultas

def marcar_consulta(usuario, data, horario):
    consultas = carregar_consultas()
    data_str = data.strftime('%d/%m/%Y')
    for consulta in consultas:
        if consulta['cpf'] == usuario['cpf'] and consulta['data'] == data_str and consulta['horario'] == horario:
            return None
    nova_consulta = {"cpf": usuario['cpf'], "data": data_str, "horario": horario}
    consultas.append(nova_consulta)
    salvar_consultas(consultas)
    return nova_consulta

def listar_consultas(usuario):
    consultas = carregar_consultas()
    return [c for c in consultas if c['cpf'] == usuario['cpf']]

def cancelar_consulta(usuario, indice):
    consultas = carregar_consultas()
    consultas_usuario = [c for c in consultas if c['cpf'] == usuario['cpf']]
    if 0 <= indice < len(consultas_usuario):
        consulta_para_remover = consultas_usuario[indice]
        consultas = [c for c in consultas if c != consulta_para_remover]
        salvar_consultas(consultas)
        return True
    return False
