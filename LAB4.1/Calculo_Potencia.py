#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Calculo_Potencia
# Author: Barrios-Tirado
# Copyright: Uis
# GNU Radio version: 3.9.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import Modulos_J1A



from gnuradio import qtgui

class Calculo_Potencia(gr.top_block, Qt.QWidget):

    def __init__(self, l_vect=1024):
        gr.top_block.__init__(self, "Calculo_Potencia", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Calculo_Potencia")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Calculo_Potencia")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Parameters
        ##################################################
        self.l_vect = l_vect

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.potencia_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.potencia_1.set_update_time(0.10)
        self.potencia_1.set_title("Potencia logaritmica (dBW)")

        labels = ['Potencia', '', '', '', '',
            '', '', '', '', '']
        units = ['(dBw)', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.potencia_1.set_min(i, -1)
            self.potencia_1.set_max(i, 1)
            self.potencia_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.potencia_1.set_label(i, "Data {0}".format(i))
            else:
                self.potencia_1.set_label(i, labels[i])
            self.potencia_1.set_unit(i, units[i])
            self.potencia_1.set_factor(i, factor[i])

        self.potencia_1.enable_autoscale(True)
        self._potencia_1_win = sip.wrapinstance(self.potencia_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._potencia_1_win)
        self.potencia3 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.potencia3.set_update_time(0.10)
        self.potencia3.set_title("Potencia logaritmica (w)")

        labels = ['Potencia', '', '', '', '',
            '', '', '', '', '']
        units = ['(w)', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.potencia3.set_min(i, -1)
            self.potencia3.set_max(i, 1)
            self.potencia3.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.potencia3.set_label(i, "Data {0}".format(i))
            else:
                self.potencia3.set_label(i, labels[i])
            self.potencia3.set_unit(i, units[i])
            self.potencia3.set_factor(i, factor[i])

        self.potencia3.enable_autoscale(False)
        self._potencia3_win = sip.wrapinstance(self.potencia3.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._potencia3_win)
        self.potencia = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.potencia.set_update_time(0.10)
        self.potencia.set_title("Potencia logaritmica (dBm)")

        labels = ['Potencia', '', '', '', '',
            '', '', '', '', '']
        units = ['(dBm)', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.potencia.set_min(i, -1)
            self.potencia.set_max(i, 1)
            self.potencia.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.potencia.set_label(i, "Data {0}".format(i))
            else:
                self.potencia.set_label(i, labels[i])
            self.potencia.set_unit(i, units[i])
            self.potencia.set_factor(i, factor[i])

        self.potencia.enable_autoscale(True)
        self._potencia_win = sip.wrapinstance(self.potencia.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._potencia_win)
        self.fft_vxx_0 = fft.fft_vfc(l_vect, True, window.blackmanharris(1024), True, 1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, l_vect)
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 30)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(1/(2*135115.625))
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(l_vect)
        self.Modulos_J1A_Sumavector_0 = Modulos_J1A.Sumavector(l_vect)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.Modulos_J1A_Sumavector_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.Modulos_J1A_Sumavector_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_nlog10_ff_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.potencia3, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.potencia, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.potencia_1, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self, 0), (self.blocks_stream_to_vector_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Calculo_Potencia")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_l_vect(self):
        return self.l_vect

    def set_l_vect(self, l_vect):
        self.l_vect = l_vect

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--l-vect", dest="l_vect", type=intx, default=1024,
        help="Set longitudFFT [default=%(default)r]")
    return parser


def main(top_block_cls=Calculo_Potencia, options=None):
    if options is None:
        options = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(l_vect=options.l_vect)

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
