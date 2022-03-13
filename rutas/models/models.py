import string
from odoo import models, fields, api, exceptions
from datetime import date
from dateutil.relativedelta import *

class ruta(models.Model):
    _name = 'rutas.ruta'
    _description = 'Coleccion de rutas.' 

    #atributos
    idRuta = fields.Integer(string='Id ', required=True)
    dirSalida = fields.Char(string='Comienzo ruta:  ',required=True)
    dirEntrega = fields.Char(string='Fin ruta: ',required=True)
    tipoViaje = fields.Selection(string='Tipo viaje', selection=[('a', 'Viaje corto'), ('b','Viaje medio'),('c','Viaje largo.')], required=True)
    #relaccion 
    camion_id = fields.Many2many('rutas.camion',string='Camiones:')

class camion(models.Model):
    _name = 'rutas.camion'
    _description = 'Camion disponibles.'

    #atributos
    idCamion = fields.Char(string='ID:',required=True)
    numBastidor = fields.Char(string='N bastidor',required=True)
    matricula = fields.Char(string='Matricula',required=True)
    #relaccion
    ruta_ids = fields.Many2many('rutas.ruta',string='Rutas:')
    trabajador_id = fields.Many2one('tiendas.trabajador',String="Trabajadores:")
    #validacion

