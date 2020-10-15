extern double STnlm_integrand_help(double phi, double X, double xsi,
                                   double density, int n, int l, int m);

extern double c_Snlm_integrand(double phi, double X, double xsi,
                               double density, int n, int l, int m);

extern double c_Tnlm_integrand(double phi, double X, double xsi,
                               double density, int n, int l, int m);

extern void c_STnlm_discrete(double *s, double *phi, double *X, double *m_k, int K,
                             int n, int l, int m, double *ST);

extern void c_STnlm_var_discrete(double *s, double *phi, double *X, double *m_k, int K,
                                 int n, int l, int m, double *ST_var);

#ifndef M_PI
    #define M_PI 3.14159265358979323846
#endif