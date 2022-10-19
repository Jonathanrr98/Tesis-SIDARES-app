export const ConsumirApi = async (tarea) => {
    try {
        let url = `http://127.0.0.1:8000/api/ambiguedades/?text=${tarea}`
        const response = await  fetch (url);
        const data = response.json()
        console.log(data)
        return data
    } catch (error) {
        
    }

}
