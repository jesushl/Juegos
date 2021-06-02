class Jadinero{
    /// Esta es una clase de Jardinero 
    /// El jardinero puede cobrar un jardin
    // El jardinero puede cobrar una poda
    // El jardinero puede cobrar un abono
    double cobro_jardin;
    double cobro_poda;
    double cobro_abono;
    String primer_nombre;
    String apehido;

    public  Jadinero(String nombre_arg, String apehido_arg){
        this.primer_nombre = nombre_arg;
        this.apehido = apehido_arg;
    }

    public double  cobrar(int numero_jardines){
        return numero_jardines * this.getCobroJardin();
    }
    public double  cobrar(int numero_jardin, int numero_podas ){
        double cobro_por_jardin = this.cobrar(numero_jardin);
        return cobro_por_jardin + ( numero_podas * this.getCobroPoda() );
    }
    public double cobrar(int numero_jardines, int numero_podas, int numero_abonos){
        double cobro_jardin_y_podas = this.cobrar(numero_jardines, numero_podas);
        return  cobro_jardin_y_podas + ( numero_abonos * this.getCobroAbono() );
    }

    public void setCobroJardin(double costo){
        this.cobro_jardin = costo;
    }
    public void setCobroPoda(double costo){
        this.cobro_poda = costo;
    }
    public void setCobroAbono(double costo){
        this.cobro_abono=costo;
    }
    public double getCobroJardin(){
        return this.cobro_jardin;
    }
    public double getCobroPoda(){
        return this.cobro_poda;
    }
    public double getCobroAbono(){
        return this.cobro_abono;
    }
}








jaimito_el_jardinero = Jardinero(nombre_arg="Jaimito", apehido_arg="eljardienro");
