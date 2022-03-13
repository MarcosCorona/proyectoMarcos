import string
from odoo import models, fields, api, exceptions
from datetime import date
from dateutil.relativedelta import *

class tienda(models.Model):
    _name = 'tiendas.tienda'
    _description = 'Define los datos de cada tienda.' 

    #atributos
    idTienda = fields.Integer(string='Id ', required=True)
    nombreTienda = fields.Char(string='Nombre tienda ',required=True)
    direccionTienda = fields.Char(string='Direccion tienda ',required=True)
    #relaccion 
    trabajador_id = fields.One2many('tiendas.trabajador','tienda_id', string='Trabajador')
    

class trabajador(models.Model):
    _name = 'tiendas.trabajador'
    _description = 'Atributos de trabajador por tienda.'

    #atributos
    dniTrabajador = fields.Char(string='DNI',required=True)
    nombreTrabajador = fields.Char(string='Nombre',required=True)
    correoTrabajador = fields.Char(string='Correo',required=True)
    fechaNacimiento = fields.Date(string='Fecha nacimiento', required=True, default = fields.date.today())
    edad = fields.Integer('Edad', compute='_getEdad')
    #relaccion
    tienda_id = fields.Many2one('tiendas.tienda', string='Tienda')
    camion_id = fields.One2many('rutas.camion_id', string='Camion')
    #validacion

    @api.constrains('dniTrabajador')
    def _checkDNI(self):
        for trabajador in self:
            if (len(trabajador.dniTrabajador) > 9 ):
                raise exceptions.ValidationError("El DNI no puede ser superior 9 caracteres.")
            if (len(trabajador.dniTrabajador) < 9):
                raise exceptions.ValidationError("El DNI no puede tener menos de 9 caracteres.")
            if(trabajador.edad < 18):
                raise exceptions.ValidationError("El trabajador no puede ser menor de edad.")

    @api.depends('fechaNacimiento')
    def _getEdad(self):
        hoy = date.today()
        for trabajador in self:
            trabajador.edad = relativedelta(hoy, trabajador.fechaNacimiento).years

    @api.constrains('edad')
    def _checkEdad(self):
        for trabajador in self:
            if(trabajador.edad < 18):
                raise exceptions.ValidationError("La edad no puede ser inferior a 18.")