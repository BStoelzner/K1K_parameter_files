# add this to the for loop starting in line 789 in montepython/data.py
# for elem in self.get_mcmc_parameters(['cosmo']):

    # infer sigma8 from h, omega_b, and omega_cdm (assuming one standard massive neutrino and omega_nu=m_nu/93.14) and S_8
    if elem == 'S_8':
        h = self.cosmo_arguments['h']
        omega_b = self.cosmo_arguments['omega_b']
        omega_cdm = self.cosmo_arguments['omega_cdm']
        try:
            omega_nu = self.cosmo_arguments['m_ncdm'] / 93.14
        except:
            omega_nu = 0.
        self.cosmo_arguments['sigma8'] = self.cosmo_arguments['S_8'] * math.sqrt((0.3*h*h) / (omega_b+omega_cdm+omega_nu))
        del self.cosmo_arguments[elem]
    # infer eta_0 from c_min, a_0, and a_1
    if elem == 'c_min':
        c_min = self.cosmo_arguments['c_min']
        # if a_0 and a_1 are not defined use the standard values given in equation (30) in Mead et al. 2015
        try:
            a_0 = self.cosmo_arguments['a_0']
        except:
            a_0 = 1.03
        try:
            a_1 = self.cosmo_arguments['a_1']
        except:
            a_1 = -0.11
        self.cosmo_arguments['eta_0'] = a_0 + a_1 * c_min
        del self.cosmo_arguments['a_0']
        del self.cosmo_arguments['a_1']
